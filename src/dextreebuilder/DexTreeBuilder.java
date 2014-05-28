/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package dextreebuilder;

import dex.*;
import dex.io.*;
import dextreebuilder.Constants;
import dex.io.instructions.DecodedInstruction;
import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Set;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author virusanalyst1
 */
public class DexTreeBuilder {

    private static ClassDef currentClass;
    private static ClassData.Method currentMethod;
    private static Dex dex;
    private static PrintWriter out;
    private static Set<Integer> methodIds;
    private static Set<Integer> fieldIds;
    private static int opcode;

    /**
     * @param args the command line arguments
     */
    private static String location() {
        String className = dex.typeNames().get(currentClass.getTypeIndex());
        if (currentMethod != null) {
            MethodId methodId = dex.methodIds().get(currentMethod.getMethodIndex());
            return className + "." + dex.strings().get(methodId.getNameIndex());
        } else {
            return className;
        }
    }

    public static void main(String[] args) {
        CodeReader codeReader = new CodeReader();
        try {
            dex = new Dex(new File("classes.dex"));
            ClassData classData = null;
//            for (String str: dex.strings())
//                System.out.println(str);
            for (ClassDef classDef : dex.classDefs()) {
                currentClass = classDef;
                currentMethod = null;
                if (classDef.getClassDataOffset() == 0) {
                    continue;
                }
                classData = dex.readClassData(classDef);
                String className = dex.typeNames().get(classDef.getTypeIndex());
                if (!className.contains("support/v4/"))
                    System.out.println("class: " + className);
                for (ClassData.Method method : classData.allMethods()) {
                    currentMethod = method;
                    int methodIndex = method.getMethodIndex();
                    if (className.contains("support/v4/")) {
                        continue;
                    }
                    System.out.println("\t method: " + dex.methodIds().get(methodIndex));
//                    System.out.println(location() + " method declared " + dex.methodIds().get(methodIndex));
                    if (method.getCodeOffset() != 0) {
                        for (DecodedInstruction inst : DecodedInstruction.decodeAll(dex.readCode(method).getInstructions())) {
                            if (inst != null) {
                                opcode = inst.getOpcode();
                                if ((opcode >= Constants.CALL_VIRTUAL
                                        && opcode <= Constants.CALL_INTERFACE)
                                        || (opcode >= Constants.CALL_VIRTUAL_R
                                        && opcode <= Constants.CALL_INTERFACE_R)) {
//                                    System.out.println(OpcodeInfo.getName(inst.getOpcode()));
                                    System.out.println("\t\t" + dex.strings().get(dex.nameIndexFromMethodIndex(inst.getIndex())));
//                                    System.out.println(dex.methodIds().get(inst.getIndex()));
                                }
                            }
                        }
                    }
                }
            }
        } catch (IOException ex) {
            Logger.getLogger(DexTreeBuilder.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
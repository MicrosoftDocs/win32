---
title: P-states and C-States
description: P-states and C-States
ms.assetid: 'fd784653-0cef-4b86-9d93-53117d654571'
---

# P-states and C-States

Processor power management technologies are defined in the ACPI specification and are divided into two categories or states:

1.  Power performance states (ACPI P states)

    P-states provide a way to scale the frequency and voltage at which the processor runs so as to reduce the power consumption of the CPU. The number of available P-states can be different for each model of CPU, even those from the same family.

2.  Processor idle sleep states (ACPI C states)

    C-states are states when the CPU has reduced or turned off selected functions. Different processors support different numbers of C-states in which various parts of the CPU are turned off. To better understand the C-states that are supported and exposed, contact the CPU vendor. Generally, higher C-states turn off more parts of the CPU, which significantly reduce power consumption. Processors may have deeper C-states that are not exposed to the operating system.

 

 





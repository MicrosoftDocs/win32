---
description: DEP/NX Protection
ms.assetid: 92F628E4-6106-42F7-B868-A3101C7A3F0A
title: DEP/NX Protection
ms.topic: article
ms.date: 05/31/2018
---

# DEP/NX Protection

Starting with Windows Internet Explorer 7 on Windows Vista, the Internet control panel item includes an **Enable memory protection** option to help mitigate online attacks. This option is also referred to as *Data Execution Prevention* (DEP) or *No-Execute* (NX). When this option is enabled, it works with the processor to help prevent buffer overflow attacks by blocking code execution from memory that is marked as non-executable.

In Windows Internet Explorer 8 on the Windows Vista with Service Pack 1 (SP1) operating system or a later version, this option is enabled by default. DEP/NX does not protect against all memory-based vulnerabilities. But when it is combined with other technologies like Address Space Layout Randomization (ASLR), it helps prevent common buffer overflow vulnerabilities in Windows Internet Explorer and the add-ons that it loads. No additional user interaction is required to provide this protection, and no new prompts are introduced.

## Related topics

<dl> <dt>

[Fixing Compatibility Issues in Web Applications by Using Compatibility View](remediating-web-applications-and-add-ons.md)
</dt> </dl>

 

 




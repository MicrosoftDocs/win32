---
Description: 'If you provide counters on a 64-bit computer, you must install both the 32-bit and 64-bit version of your provider on the computer if you want to support both 32-bit and 64-bit consumers.'
ms.assetid: '2dba2c46-0185-4ce6-a7cc-27cdd9b19b70'
title: '64-bit Support'
---

# 64-bit Support

If you provide counters on a 64-bit computer, you must install both the 32-bit and 64-bit version of your provider on the computer if you want to support both 32-bit and 64-bit consumers. Place the 32-bit version in the %windir%\\syswow64 folder and the 64-bit version in the %windir%\\system32 folder.

For a 32-bit consumer to consume counter data, the 32-bit version of the provider must exist on the 32-bit computer and 64-bit computer.

For a 64-bit consumer to consume counter data, the 64-bit version of the provider must exist on the 64-bit computer. (You cannot run a 64-bit consumer on a 32-bit computer.)

For a 32-bit consumer to consume remote counter data from a 32-bit computer, the 32-bit version of the provider must exist on the remote computer. A 32-bit consumer can consume remote counter data from a 64-bit computer only if the remote computer contains the 64-bit version of the provider.

For a 64-bit consumer to consume remote counter data from a 32-bit computer, the 32-bit version of the provider must exist on the remote computer. A 64-bit consumer can consume remote counter data from a 64-bit computer only if the remote computer contains the 64-bit version of the provider.

 

 




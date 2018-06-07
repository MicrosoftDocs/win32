---
Description: A database field of the FormattedSDDLText data type holds a text string that describes a security descriptor using valid security descriptor definition language (SDDL.) This data type is used by the SDDLText field of the MsiLockPermissionsEx Table to secure a selected object. Note that the SDDLText field of the MsiLockPermissionsEx Table does not support private or public properties.
ms.assetid: a36e257d-ef3c-45db-a50e-94d7fd4e09e2
title: FormattedSDDLText
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FormattedSDDLText

A database field of the **FormattedSDDLText** data type holds a text string that describes a security descriptor using valid [security descriptor definition language](https://msdn.microsoft.com/2b15325e-34ed-497b-ae6d-3ec3ac168232) (SDDL.) This data type is used by the SDDLText field of the [MsiLockPermissionsEx Table](msilockpermissionsex-table.md) to secure a selected object. Note that the SDDLText field of the MsiLockPermissionsEx Table does not support private or public properties.

**[Windows Installer 4.5 or earlier](not-supported-in-windows-installer-4-5.md):** Not supported. This data type is available beginning with Windows Installer 5.0.

The **FormattedSDDLText** data type can hold a SDDL string written in valid [Security Descriptor String Format](https://msdn.microsoft.com/0a226629-084c-40c5-bdd4-ad7355c807cf). For more information about SDDL, see the [Access Control](https://msdn.microsoft.com/d9ce4ec5-5c09-4b33-93a1-39638a925986) section of the [Microsoft Windows Software Development Kit (SDK)](http://go.microsoft.com/fwlink/p/?linkid=162443). In addition, a **FormattedSDDLText** text string can use angle brackets (&lt;&gt;) to contain the domain and user name of the user whose account SID is to be determined.

If the user having user name *SampleUser* belongs to a domain named *SampleDomain*, then the **FormattedSDDLText** value can identify the owner using the SID string, the user name and domain name, or the Windows environment variables. For example, the following strings would be possible.

<dl> O:*owner\_sid\_string*G:BAD:(D;OICI;GA;;;BG)(A;OICI;GRGWGX;;;*owner\_sid\_string*)(A;OICI;GA;;;BA)S:ARAI(AU;SAFA;FA;;;WD)  
O:&lt;*SampleDomain\\SampleUser*&gt;G:BAD:(D;OICI;GA;;;BG)(A;OICI;GRGWGX;;;&lt;*SampleDomain\\SampleUser*&gt;)(A;OICI;GA;;;BA)S:ARAI(AU;SAFA;FA;;;WD)  
O:&lt;\[%USERDOMAIN\]\\\[%USERNAME\]&gt;G:BAD:(D;OICI;GA;;;BG)(A;OICI;GRGWGX;;;&lt;\[%USERDOMAIN\]\\\[%USERNAME\]&gt;)(A;OICI;GA;;;BA)S:ARAI(AU;SAFA;FA;;;WD)  
</dl>

 

 




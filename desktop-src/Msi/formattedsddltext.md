---
Description: 'A database field of the FormattedSDDLText data type holds a text string that describes a security descriptor using valid security descriptor definition language (SDDL.) This data type is used by the SDDLText field of the MsiLockPermissionsEx Table to secure a selected object. Note that the SDDLText field of the MsiLockPermissionsEx Table does not support private or public properties.'
ms.assetid: 'a36e257d-ef3c-45db-a50e-94d7fd4e09e2'
title: FormattedSDDLText
---

# FormattedSDDLText

A database field of the **FormattedSDDLText** data type holds a text string that describes a security descriptor using valid [security descriptor definition language](security.security_descriptor_definition_language) (SDDL.) This data type is used by the SDDLText field of the [MsiLockPermissionsEx Table](msilockpermissionsex-table.md) to secure a selected object. Note that the SDDLText field of the MsiLockPermissionsEx Table does not support private or public properties.

**[Windows Installer 4.5 or earlier](not-supported-in-windows-installer-4-5.md):** Not supported. This data type is available beginning with Windows Installer 5.0.

The **FormattedSDDLText** data type can hold a SDDL string written in valid [Security Descriptor String Format](security.security_descriptor_string_format). For more information about SDDL, see the [Access Control](security.access_control) section of the [Microsoft Windows Software Development Kit (SDK)](http://go.microsoft.com/fwlink/p/?linkid=162443). In addition, a **FormattedSDDLText** text string can use angle brackets (&lt;&gt;) to contain the domain and user name of the user whose account SID is to be determined.

If the user having user name *SampleUser* belongs to a domain named *SampleDomain*, then the **FormattedSDDLText** value can identify the owner using the SID string, the user name and domain name, or the Windows environment variables. For example, the following strings would be possible.

<dl> O:*owner\_sid\_string*G:BAD:(D;OICI;GA;;;BG)(A;OICI;GRGWGX;;;*owner\_sid\_string*)(A;OICI;GA;;;BA)S:ARAI(AU;SAFA;FA;;;WD)  
O:&lt;*SampleDomain\\SampleUser*&gt;G:BAD:(D;OICI;GA;;;BG)(A;OICI;GRGWGX;;;&lt;*SampleDomain\\SampleUser*&gt;)(A;OICI;GA;;;BA)S:ARAI(AU;SAFA;FA;;;WD)  
O:&lt;\[%USERDOMAIN\]\\\[%USERNAME\]&gt;G:BAD:(D;OICI;GA;;;BG)(A;OICI;GRGWGX;;;&lt;\[%USERDOMAIN\]\\\[%USERNAME\]&gt;)(A;OICI;GA;;;BA)S:ARAI(AU;SAFA;FA;;;WD)  
</dl>

 

 




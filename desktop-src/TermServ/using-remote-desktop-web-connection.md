---
title: Using the Remote Desktop ActiveX control
description: How you can use the Remote Desktop ActiveX control to customize the Remote Desktop Services user experience.
ms.assetid: ea80a99a-7bf6-48e2-8bd0-c9a158bcf475
ms.tgt_platform: multiple
keywords:
- Remote Desktop Services Remote Desktop Services , using Remote Desktop ActiveX control
- Remote Desktop Web Connection Remote Desktop Services , using
- Remote Desktop Protocol Remote Desktop Services
ms.topic: article
ms.date: 05/31/2018
---

# Using the Remote Desktop ActiveX control

The following topics contain information about how you can use the Remote Desktop ActiveX control to customize the Remote Desktop Services user experience.

The Remote Desktop ActiveX control is available in the following forms:

-   **The scriptable control**—implements interfaces that are safe for scripting. This form of the control can be used by web clients or scripting (such as VBScript) hosts.
-   **The nonscriptable control**—offers additional functionality that is not safe for scripting. This form of the control can be used from native or managed code, but this form cannot be used by web clients or scripting-only hosts.

The following list contains the **CLSID**s for the different controls for different operating system versions. Each of the **CLSID**s is compatible with later system versions. For example, the **CLSID** for the scriptable control on Windows Vista will work on later system versions, such as Windows 7.



| System version                          | Scriptable control CLSID             | Nonscriptable control CLSID          |
|-----------------------------------------|--------------------------------------|--------------------------------------|
| Windows 8.1, Windows Server 2012 R2     | 301B94BA-5D25-4A12-BFFE-3B6E7A616585 | 8B918B82-7985-4C24-89DF-C33AD2BBFBCD |
| Windows 8, Windows Server 2012          | 5F681803-2900-4C43-A1CC-CF405404A676 | A3BC03A0-041D-42E3-AD22-882B7865C9C5 |
| Windows 7, Windows Server 2008          | A9D7038D-B5ED-472E-9C47-94BEA90A5910 | 54D38BF7-B1EF-4479-9674-1BD6EA465258 |
| Windows Vista with Service Pack 1 (SP1) | 7390F3D8-0439-4C05-91E3-CF5CB290C3D0 | D2EA46A7-C2BF-426B-AF24-E19C44456399 |
| Windows Vista                           | 4EB89FF4-7F78-4A0F-8B8D-2BF02E94E4B2 | 4EB2F086-C818-447E-B32C-C51CE2B30D31 |



 

## In this section

<dl> <dt>

[Embedding the Remote Desktop ActiveX control in a webpage](embedding-the-remote-desktop-activex-control-in-a-web-page.md)
</dt> <dd>

Example that demonstrates the use of the scriptable interfaces.

</dd> <dt>

[Implementing scriptable virtual channels by using Remote Desktop Web Connection](implementing-scriptable-virtual-channels-using-remote-desktop-web-connection.md)
</dt> <dd>

Code examples that show the steps for implementing scriptable virtual channels with Remote Desktop Web Connection.

</dd> <dt>

[Using the Remote Desktop ActiveX control with virtual channels](using-the-remote-desktop-activex-control-with-virtual-channels.md)
</dt> <dd>

If you have enabled a virtual channels application in your Remote Desktop Services deployment, you can make this application available to client computers.

</dd> <dt>

[Sample webpage included with the Remote Desktop ActiveX control](sample-web-page-included-with-the-remote-desktop-activex-control.md)
</dt> <dd>

A sample webpage (Default.htm) is in the directory where Remote Desktop Web Connection is installed.

</dd> <dt>

[Providing for RDP client security](providing-for-rdp-client-security.md)
</dt> <dd>

Some properties of the Remote Desktop ActiveX control object are restricted to specific Internet Explorer URL security zones.

</dd> <dt>

[Disabling Remote Desktop Services features](disabling-terminal-services-features.md)
</dt> <dd>

For enhanced security, you might choose to disable Remote Desktop Services features.

</dd> </dl>

For more information about the sample webpage that is included with the installation of the Remote Desktop ActiveX control, see [Sample webpage included with the Remote Desktop ActiveX control](sample-web-page-included-with-the-remote-desktop-activex-control.md).

 

 





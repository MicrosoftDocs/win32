---
Description: '.'
ms.assetid: '88810916-A85E-4EC7-A6AE-1CA2A2205DBC'
title: Protected Mode
---

# Protected Mode

Most Windows Internet Explorer 8 security features are available in Internet Explorer 8 for the Windows XP with Service Pack 2 (SP2) operating system and later versions. Protected Mode is available only for Windows Vista or later versions because it is based on the following security features that are new to Windows Vista:

-   [User Account Control (UAC)](http://go.microsoft.com/fwlink/p/?linkid=205674) makes it easy to run without administrator privileges. When users run programs with limited user privileges, they are safer from an attack than when they run with administrator privileges. The Windows operating system can restrict the malicious code from carrying out damaging actions.
-   An integrity mechanism restricts write access to [securable objects](security.securable_objects) by lower-integrity processes, in the same way that user account group membership restricts the rights of users to access sensitive system components.
-   [User Interface Privilege Isolation (UIPI)](bc42695d-2bd3-4a7f-ac8f-bd3dac86e399) prevents processes from sending selected window messages and other USER APIs to processes that are running with higher integrity.

The Windows Integrity Mechanism security infrastructure allows Protected Mode to provide Windows Internet Explorer with the privileges that users need to browse the web, while withholding privileges that users need to install programs silently or modify sensitive system data.

Users can disable this feature through a check box, and administrators can disable it by using Group Policy.

> \[!Important\]  
> You should disable the feature only as a temporary measure during troubleshooting to compare behavior of the application when the feature is enabled or not. We recommended that you keep this feature permanently enabled.

 

## Related topics

<dl> <dt>

[Fixing Compatibility Issues in Web Applications by Using Compatibility View](remediating-web-applications-and-add-ons.md)
</dt> </dl>

 

 




---
Description: The Windows security model enables you to control access to registry keys. For more information about security, see Access-Control Model.
ms.assetid: 266d5c8e-1bcd-48e5-bc06-2fbc956d8658
title: Registry Key Security and Access Rights
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Registry Key Security and Access Rights

The Windows security model enables you to control access to registry keys. For more information about security, see [Access-Control Model](https://msdn.microsoft.com/library/windows/desktop/aa374876).

You can specify a [security descriptor](https://msdn.microsoft.com/library/windows/desktop/aa379563) for a registry key when you call the [**RegCreateKeyEx**](/windows/desktop/api/Winreg/nf-winreg-regcreatekeyexa) or [**RegSetKeySecurity**](https://msdn.microsoft.com/library/windows/desktop/aa379314) function. If you specify **NULL**, the key gets a default security descriptor. The ACLs in a default security descriptor for a key are inherited from its direct parent key.

To get the security descriptor of a registry key, call the [**RegGetKeySecurity**](https://msdn.microsoft.com/library/windows/desktop/aa379313), [**GetNamedSecurityInfo**](https://msdn.microsoft.com/library/windows/desktop/aa446645), or [**GetSecurityInfo**](https://msdn.microsoft.com/library/windows/desktop/aa446654) function.

The valid access rights for registry keys include the DELETE, READ\_CONTROL, WRITE\_DAC, and WRITE\_OWNER [standard access rights](https://msdn.microsoft.com/library/windows/desktop/aa379607). Registry keys do not support the SYNCHRONIZE standard access right.

The following table lists the specific access rights for registry key objects.



| Value                                         | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| KEY\_ALL\_ACCESS (0xF003F)<br/>         | Combines the STANDARD\_RIGHTS\_REQUIRED, KEY\_QUERY\_VALUE, KEY\_SET\_VALUE, KEY\_CREATE\_SUB\_KEY, KEY\_ENUMERATE\_SUB\_KEYS, KEY\_NOTIFY, and KEY\_CREATE\_LINK access rights.<br/>                                                                                                                                                                                                                                                                           |
| KEY\_CREATE\_LINK (0x0020)<br/>         | Reserved for system use.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| KEY\_CREATE\_SUB\_KEY (0x0004)<br/>     | Required to create a subkey of a registry key.<br/>                                                                                                                                                                                                                                                                                                                                                                                                             |
| KEY\_ENUMERATE\_SUB\_KEYS (0x0008)<br/> | Required to enumerate the subkeys of a registry key.<br/>                                                                                                                                                                                                                                                                                                                                                                                                       |
| KEY\_EXECUTE (0x20019)<br/>             | Equivalent to KEY\_READ.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| KEY\_NOTIFY (0x0010)<br/>               | Required to request change notifications for a registry key or for subkeys of a registry key.<br/>                                                                                                                                                                                                                                                                                                                                                              |
| KEY\_QUERY\_VALUE (0x0001)<br/>         | Required to query the values of a registry key.<br/>                                                                                                                                                                                                                                                                                                                                                                                                            |
| KEY\_READ (0x20019)<br/>                | Combines the STANDARD\_RIGHTS\_READ, KEY\_QUERY\_VALUE, KEY\_ENUMERATE\_SUB\_KEYS, and KEY\_NOTIFY values.<br/>                                                                                                                                                                                                                                                                                                                                                 |
| KEY\_SET\_VALUE (0x0002)<br/>           | Required to create, delete, or set a registry value.<br/>                                                                                                                                                                                                                                                                                                                                                                                                       |
| KEY\_WOW64\_32KEY (0x0200)<br/>         | Indicates that an application on 64-bit Windows should operate on the 32-bit registry view. This flag is ignored by 32-bit Windows. For more information, see [Accessing an Alternate Registry View](https://msdn.microsoft.com/library/windows/desktop/aa384129).<br/> This flag must be combined using the OR operator with the other flags in this table that either query or access registry values.<br/> **Windows 2000:** This flag is not supported.<br/> |
| KEY\_WOW64\_64KEY (0x0100)<br/>         | Indicates that an application on 64-bit Windows should operate on the 64-bit registry view. This flag is ignored by 32-bit Windows. For more information, see [Accessing an Alternate Registry View](https://msdn.microsoft.com/library/windows/desktop/aa384129).<br/> This flag must be combined using the OR operator with the other flags in this table that either query or access registry values.<br/> **Windows 2000:** This flag is not supported.<br/> |
| KEY\_WRITE (0x20006)<br/>               | Combines the STANDARD\_RIGHTS\_WRITE, KEY\_SET\_VALUE, and KEY\_CREATE\_SUB\_KEY access rights.<br/>                                                                                                                                                                                                                                                                                                                                                            |



 

When you call the [**RegOpenKeyEx**](/windows/desktop/api/Winreg/nf-winreg-regopenkeyexa) function, the system checks the requested access rights against the key's security descriptor. If the user does not have the correct access to the registry key, the open operation fails. If an administrator needs access to the key, the solution is to enable the SE\_TAKE\_OWNERSHIP\_NAME privilege and open the registry key with WRITE\_OWNER access. For more information, see [Enabling and Disabling Privileges](https://msdn.microsoft.com/library/windows/desktop/aa446619).

You can request the ACCESS\_SYSTEM\_SECURITY access right to a registry key if you want to read or write the key's system access control list (SACL). For more information, see [Access-Control Lists (ACLs)](https://msdn.microsoft.com/library/windows/desktop/aa374872) and [SACL Access Right](https://msdn.microsoft.com/library/windows/desktop/aa379321).

To view the current access rights for a key, including the predefined keys, use the Registry Editor (Regedt32.exe). After navigating to the desired key, go to the **Edit** menu and select **Permissions**.

 

 





---
Description: Native Wifi API Permissions
ms.assetid: cfea9f7d-a069-497b-8138-b3949002fa5d
title: Native Wifi API Permissions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Native Wifi API Permissions

A Native Wifi API call may fail with when a caller does not have adequate permissions to perform the requested operation.

Permissions are stored in a [discretionary access control lists (DACL)](https://msdn.microsoft.com/c9aff246-fe11-4d82-b944-b10c3d9ae170) associated with a [**WLAN\_SECURABLE\_OBJECT**](/windows/desktop/api/wlanapi/ne-wlanapi-_wlan_securable_object). For more information about DACLs and securable objects, see [How DACLs Control Access to an Object](https://msdn.microsoft.com/dc98b23e-ce42-4d4a-a285-c0b7b5e2a478).

The following table shows the Native Wifi functions that use securable objects to determine if the caller has sufficient permissions to perform the requested operation. It also shows the securable objects used by each function.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Securable object</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>WlanGetFilterList</strong>](/windows/desktop/api/wlanapi/nf-wlanapi-wlangetfilterlist), [<strong>WlanSetFilterList</strong>](/windows/desktop/api/wlanapi/nf-wlanapi-wlansetfilterlist)<br/></td>
<td><ul>
<li>wlan_secure_deny_list</li>
<li>wlan_secure_permit_list</li>
</ul></td>
</tr>
<tr class="even">
<td>[<strong>WlanIhvControl</strong>](/windows/desktop/api/wlanapi/nf-wlanapi-wlanihvcontrol)<br/></td>
<td><ul>
<li>wlan_secure_ihv_control</li>
</ul></td>
</tr>
<tr class="odd">
<td>[<strong>WlanQueryAutoConfigParameter</strong>](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanqueryautoconfigparameter), [<strong>WlanSetAutoConfigParameter</strong>](/windows/desktop/api/Wlanapi/nf-wlanapi-wlansetautoconfigparameter)<br/></td>
<td><ul>
<li>wlan_secure_show_denied</li>
</ul></td>
</tr>
<tr class="even">
<td>[<strong>WlanQueryInterface</strong>](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanqueryinterface), [<strong>WlanSetInterface</strong>](/windows/desktop/api/Wlanapi/nf-wlanapi-wlansetinterface)<br/></td>
<td><ul>
<li>wlan_secure_ac_enabled</li>
<li>wlan_secure_bc_scan_enabled</li>
<li>wlan_secure_bss_type</li>
<li>wlan_secure_current_operation_mode</li>
<li>wlan_secure_interface_properties</li>
<li>wlan_secure_media_streaming_mode_enabled</li>
</ul></td>
</tr>
<tr class="odd">
<td>[<strong>WlanSetProfile</strong>](/windows/desktop/api/wlanapi/nf-wlanapi-wlansetprofile)<br/></td>
<td><ul>
<li>wlan_secure_add_new_all_user_profiles</li>
<li>wlan_secure_add_new_per_user_profiles</li>
</ul></td>
</tr>
<tr class="even">
<td>[<strong>WlanSetProfileList</strong>](/windows/desktop/api/wlanapi/nf-wlanapi-wlansetprofilelist), [<strong>WlanSetProfilePosition</strong>](/windows/desktop/api/wlanapi/nf-wlanapi-wlansetprofileposition)<br/></td>
<td><ul>
<li>wlan_secure_all_user_profiles_order</li>
</ul></td>
</tr>
</tbody>
</table>



 

Before one of the above-named functions completes its operation, the function retrieves the DACL stored in the appropriate securable object. The function then checks the DACL to see if the caller has sufficient permissions. The WlanGet\* and WlanQuery\* functions require that the DACL contains an [access control entry (ACE)](https://msdn.microsoft.com/9cf4d796-3955-456b-9db9-ae9fa83752f6) that grants the [access token](https://msdn.microsoft.com/350159c9-2399-427a-ba44-c897a9664299) of the calling thread WLAN\_READ\_ACCESS to the function. The WlanSet\* functions require an ACE that grants the access token of the calling thread WLAN\_WRITE\_ACCESS. If the caller does not have sufficient permissions, the function call fails with the error ERROR\_ACCESS\_DENIED.

Each securable object has a DACL associated with it by default. The default permissions stored in the DACL can be changed using the [**WlanSetSecuritySettings**](/windows/desktop/api/wlanapi/nf-wlanapi-wlansetsecuritysettings) function. To determine the effective user rights required to perform an operation on a particular system, call [**WlanGetSecuritySettings**](/windows/desktop/api/wlanapi/nf-wlanapi-wlangetsecuritysettings).

All-user profiles have additional permissions associated with the profile itself. The permissions on an all-user profile are established when the profile is created or modified using [**WlanSetProfile**](/windows/desktop/api/wlanapi/nf-wlanapi-wlansetprofile) or [**WlanSaveTemporaryProfile**](/windows/desktop/api/wlanapi/nf-wlanapi-wlansavetemporaryprofile). The *strAllUserProfileSecurity* parameter specifies the required permissions for modifying a profile, deleting a profile, or connecting to a network using a profile. Deleting or modifying a profile requires WLAN\_WRITE\_ACCESS permission. Connecting to a network using a profile requires WLAN\_EXECUTE\_ACCESS permission.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:  ** The [**WlanGetSecuritySettings**](/windows/desktop/api/wlanapi/nf-wlanapi-wlangetsecuritysettings) and [**WlanSetSecuritySettings**](/windows/desktop/api/wlanapi/nf-wlanapi-wlansetsecuritysettings) functions are not supported. The *strAllUserProfileSecurity* parameter is not used.

## Related topics

<dl> <dt>

[How DACLs Control Access to an Object](https://msdn.microsoft.com/dc98b23e-ce42-4d4a-a285-c0b7b5e2a478)
</dt> <dt>

[**WLAN\_SECURABLE\_OBJECT**](/windows/desktop/api/wlanapi/ne-wlanapi-_wlan_securable_object)
</dt> </dl>

 

 





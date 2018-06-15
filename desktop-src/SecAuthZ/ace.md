---
Description: Lists the currently defined ACE types.
ms.assetid: 002a3fa7-02a3-4832-948e-b048f5f5818f
title: ACE
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ACE

An **ACE** is an [*access control entry*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-entry-gly) in an [*access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-list-gly) (ACL).

The following table lists the currently defined **ACE** types.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>ACE type</th>
<th>Structure</th>
<th>ACL type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li>Access allowed</li>
</ul></td>
<td>[<strong>ACCESS_ALLOWED_ACE</strong>](/windows/desktop/api/Winnt/ns-winnt-_access_allowed_ace)</td>
<td>Discretionary</td>
</tr>
<tr class="even">
<td><ul>
<li>Access allowed</li>
<li>Allows callback during access check</li>
</ul></td>
<td>[<strong>ACCESS_ALLOWED_CALLBACK_ACE</strong>](/windows/desktop/api/Winnt/ns-winnt-_access_allowed_callback_ace)</td>
<td>Discretionary</td>
</tr>
<tr class="odd">
<td><ul>
<li>Access allowed</li>
<li>Object specific</li>
</ul></td>
<td>[<strong>ACCESS_ALLOWED_OBJECT_ACE</strong>](/windows/desktop/api/Winnt/ns-winnt-_access_allowed_object_ace)</td>
<td>Discretionary</td>
</tr>
<tr class="even">
<td><ul>
<li>Access allowed</li>
<li>Object specific</li>
<li>Allows callback during access check</li>
</ul></td>
<td>[<strong>ACCESS_ALLOWED_CALLBACK_OBJECT_ACE</strong>](/windows/desktop/api/Winnt/ns-winnt-_access_allowed_callback_object_ace)</td>
<td>Discretionary</td>
</tr>
<tr class="odd">
<td><ul>
<li>Access denied</li>
</ul></td>
<td>[<strong>ACCESS_DENIED_ACE</strong>](/windows/desktop/api/Winnt/ns-winnt-_access_denied_ace)</td>
<td>Discretionary</td>
</tr>
<tr class="even">
<td><ul>
<li>Access denied</li>
<li>Allows callback during access check</li>
</ul></td>
<td>[<strong>ACCESS_DENIED_CALLBACK_ACE</strong>](/windows/desktop/api/Winnt/ns-winnt-_access_denied_callback_ace)</td>
<td>Discretionary</td>
</tr>
<tr class="odd">
<td><ul>
<li>Access denied</li>
<li>Object specific</li>
<li>Allows callback during access check</li>
</ul></td>
<td>[<strong>ACCESS_DENIED_CALLBACK_OBJECT_ACE</strong>](/windows/desktop/api/Winnt/ns-winnt-_access_denied_callback_object_ace)</td>
<td>Discretionary</td>
</tr>
<tr class="even">
<td><ul>
<li>Access denied</li>
<li>Object specific</li>
</ul></td>
<td>[<strong>ACCESS_DENIED_OBJECT_ACE</strong>](/windows/desktop/api/Winnt/ns-winnt-_access_denied_object_ace)</td>
<td>Discretionary</td>
</tr>
<tr class="odd">
<td><ul>
<li>System alarm</li>
</ul></td>
<td>[<strong>SYSTEM_ALARM_ACE</strong>](/windows/desktop/api/Winnt/ns-winnt-_system_alarm_ace)</td>
<td>System</td>
</tr>
<tr class="even">
<td><ul>
<li>System alarm</li>
<li>Allows callback during access check</li>
</ul></td>
<td>[<strong>SYSTEM_ALARM_CALLBACK_ACE</strong>](/windows/desktop/api/Winnt/ns-winnt-_system_alarm_callback_ace)</td>
<td>System</td>
</tr>
<tr class="odd">
<td><ul>
<li>System alarm</li>
<li>Object specific</li>
<li>Allows callback during access check</li>
</ul></td>
<td>[<strong>SYSTEM_ALARM_CALLBACK_OBJECT_ACE</strong>](/windows/desktop/api/Winnt/ns-winnt-_system_alarm_callback_object_ace)</td>
<td>System</td>
</tr>
<tr class="even">
<td><ul>
<li>System alarm</li>
<li>Object specific</li>
</ul></td>
<td>[<strong>SYSTEM_ALARM_OBJECT_ACE</strong>](https://msdn.microsoft.com/en-us/library/Aa379615(v=VS.85).aspx)</td>
<td>System</td>
</tr>
<tr class="odd">
<td><ul>
<li>System audit</li>
</ul></td>
<td>[<strong>SYSTEM_AUDIT_ACE</strong>](/windows/desktop/api/Winnt/ns-winnt-_system_audit_ace)</td>
<td>System</td>
</tr>
<tr class="even">
<td><ul>
<li>System audit</li>
<li>Allows callback during access check</li>
</ul></td>
<td>[<strong>SYSTEM_AUDIT_CALLBACK_ACE</strong>](/windows/desktop/api/Winnt/ns-winnt-_system_audit_callback_ace)</td>
<td>System</td>
</tr>
<tr class="odd">
<td><ul>
<li>System audit</li>
<li>Object specific</li>
<li>Allows callback during access check</li>
</ul></td>
<td>[<strong>SYSTEM_AUDIT_CALLBACK_OBJECT_ACE</strong>](/windows/desktop/api/Winnt/ns-winnt-_system_audit_callback_object_ace)</td>
<td>System</td>
</tr>
<tr class="even">
<td><ul>
<li>System audit</li>
<li>Object specific</li>
</ul></td>
<td>[<strong>SYSTEM_AUDIT_OBJECT_ACE</strong>](/windows/desktop/api/Winnt/ns-winnt-_system_alarm_object_ace)</td>
<td>System</td>
</tr>
</tbody>
</table>



 

System-alarm and object-specific system-alarm ACEs are not currently supported.

> [!Note]  
> Each ACE starts with an [**ACE\_HEADER**](/windows/desktop/api/Winnt/ns-winnt-_ace_header) structure. The format of the data following the header varies according to the ACE type specified in the header.

 

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                   |
| Header<br/>                   | <dl> <dt>Winnt.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**AddAce**](https://msdn.microsoft.com/en-us/library/Aa374970(v=VS.85).aspx)
</dt> <dt>

[**ACCESS\_ALLOWED\_ACE**](/windows/desktop/api/Winnt/ns-winnt-_access_allowed_ace)
</dt> <dt>

[**ACCESS\_DENIED\_ACE**](/windows/desktop/api/Winnt/ns-winnt-_access_denied_ace)
</dt> <dt>

[**ACL**](/windows/desktop/api/Winnt/ns-winnt-_acl)
</dt> <dt>

[**SYSTEM\_ALARM\_ACE**](/windows/desktop/api/Winnt/ns-winnt-_system_alarm_object_ace)
</dt> <dt>

[**SYSTEM\_AUDIT\_ACE**](/windows/desktop/api/Winnt/ns-winnt-_system_audit_ace)
</dt> </dl>

 

 





---
description: Lists the currently defined ACE types.
ms.assetid: '980b8242-2ba2-469f-b834-da7d3fb22e14'
title: ACE (Winnt.h)
ms.topic: article
ms.date: 05/31/2018
---

# ACE

An **ACE** is an [*access control entry*](/windows/desktop/SecGloss/a-gly) in an [*access control list*](/windows/desktop/SecGloss/a-gly) (ACL).

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
<td><a href="/windows/desktop/api/Winnt/ns-winnt-access_allowed_ace"><strong>ACCESS_ALLOWED_ACE</strong></a></td>
<td>Discretionary</td>
</tr>
<tr class="even">
<td><ul>
<li>Access allowed</li>
<li>Allows callback during access check</li>
</ul></td>
<td><a href="/windows/desktop/api/Winnt/ns-winnt-access_allowed_callback_ace"><strong>ACCESS_ALLOWED_CALLBACK_ACE</strong></a></td>
<td>Discretionary</td>
</tr>
<tr class="odd">
<td><ul>
<li>Access allowed</li>
<li>Object specific</li>
</ul></td>
<td><a href="/windows/desktop/api/Winnt/ns-winnt-access_allowed_object_ace"><strong>ACCESS_ALLOWED_OBJECT_ACE</strong></a></td>
<td>Discretionary</td>
</tr>
<tr class="even">
<td><ul>
<li>Access allowed</li>
<li>Object specific</li>
<li>Allows callback during access check</li>
</ul></td>
<td><a href="/windows/desktop/api/Winnt/ns-winnt-access_allowed_callback_object_ace"><strong>ACCESS_ALLOWED_CALLBACK_OBJECT_ACE</strong></a></td>
<td>Discretionary</td>
</tr>
<tr class="odd">
<td><ul>
<li>Access denied</li>
</ul></td>
<td><a href="/windows/desktop/api/Winnt/ns-winnt-access_denied_ace"><strong>ACCESS_DENIED_ACE</strong></a></td>
<td>Discretionary</td>
</tr>
<tr class="even">
<td><ul>
<li>Access denied</li>
<li>Allows callback during access check</li>
</ul></td>
<td><a href="/windows/desktop/api/Winnt/ns-winnt-access_denied_callback_ace"><strong>ACCESS_DENIED_CALLBACK_ACE</strong></a></td>
<td>Discretionary</td>
</tr>
<tr class="odd">
<td><ul>
<li>Access denied</li>
<li>Object specific</li>
<li>Allows callback during access check</li>
</ul></td>
<td><a href="/windows/desktop/api/Winnt/ns-winnt-access_denied_callback_object_ace"><strong>ACCESS_DENIED_CALLBACK_OBJECT_ACE</strong></a></td>
<td>Discretionary</td>
</tr>
<tr class="even">
<td><ul>
<li>Access denied</li>
<li>Object specific</li>
</ul></td>
<td><a href="/windows/desktop/api/Winnt/ns-winnt-access_denied_object_ace"><strong>ACCESS_DENIED_OBJECT_ACE</strong></a></td>
<td>Discretionary</td>
</tr>
<tr class="odd">
<td><ul>
<li>System alarm</li>
</ul></td>
<td><a href="/windows/desktop/api/Winnt/ns-winnt-system_alarm_ace"><strong>SYSTEM_ALARM_ACE</strong></a></td>
<td>System</td>
</tr>
<tr class="even">
<td><ul>
<li>System alarm</li>
<li>Allows callback during access check</li>
</ul></td>
<td><a href="/windows/desktop/api/Winnt/ns-winnt-system_alarm_callback_ace"><strong>SYSTEM_ALARM_CALLBACK_ACE</strong></a></td>
<td>System</td>
</tr>
<tr class="odd">
<td><ul>
<li>System alarm</li>
<li>Object specific</li>
<li>Allows callback during access check</li>
</ul></td>
<td><a href="/windows/desktop/api/Winnt/ns-winnt-system_alarm_callback_object_ace"><strong>SYSTEM_ALARM_CALLBACK_OBJECT_ACE</strong></a></td>
<td>System</td>
</tr>
<tr class="even">
<td><ul>
<li>System alarm</li>
<li>Object specific</li>
</ul></td>
<td><a href="/windows/desktop/api/winnt/ns-winnt-system_alarm_object_ace"><strong>SYSTEM_ALARM_OBJECT_ACE</strong></a></td>
<td>System</td>
</tr>
<tr class="odd">
<td><ul>
<li>System audit</li>
</ul></td>
<td><a href="/windows/desktop/api/Winnt/ns-winnt-system_audit_ace"><strong>SYSTEM_AUDIT_ACE</strong></a></td>
<td>System</td>
</tr>
<tr class="even">
<td><ul>
<li>System audit</li>
<li>Allows callback during access check</li>
</ul></td>
<td><a href="/windows/desktop/api/Winnt/ns-winnt-system_audit_callback_ace"><strong>SYSTEM_AUDIT_CALLBACK_ACE</strong></a></td>
<td>System</td>
</tr>
<tr class="odd">
<td><ul>
<li>System audit</li>
<li>Object specific</li>
<li>Allows callback during access check</li>
</ul></td>
<td><a href="/windows/desktop/api/Winnt/ns-winnt-system_audit_callback_object_ace"><strong>SYSTEM_AUDIT_CALLBACK_OBJECT_ACE</strong></a></td>
<td>System</td>
</tr>
<tr class="even">
<td><ul>
<li>System audit</li>
<li>Object specific</li>
</ul></td>
<td><a href="/windows/desktop/api/Winnt/ns-winnt-system_alarm_object_ace"><strong>SYSTEM_AUDIT_OBJECT_ACE</strong></a></td>
<td>System</td>
</tr>
</tbody>
</table>



 

System-alarm and object-specific system-alarm ACEs are not currently supported.

> [!Note]  
> Each ACE starts with an [**ACE\_HEADER**](/windows/desktop/api/Winnt/ns-winnt-ace_header) structure. The format of the data following the header varies according to the ACE type specified in the header.

 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                   |
| Header<br/>                   | <dl> <dt>Winnt.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**AddAce**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-addace)
</dt> <dt>

[**ACCESS\_ALLOWED\_ACE**](/windows/desktop/api/Winnt/ns-winnt-access_allowed_ace)
</dt> <dt>

[**ACCESS\_DENIED\_ACE**](/windows/desktop/api/Winnt/ns-winnt-access_denied_ace)
</dt> <dt>

[**ACL**](/windows/desktop/api/Winnt/ns-winnt-acl)
</dt> <dt>

[**SYSTEM\_ALARM\_ACE**](/windows/desktop/api/Winnt/ns-winnt-system_alarm_object_ace)
</dt> <dt>

[**SYSTEM\_AUDIT\_ACE**](/windows/desktop/api/Winnt/ns-winnt-system_audit_ace)
</dt> </dl>


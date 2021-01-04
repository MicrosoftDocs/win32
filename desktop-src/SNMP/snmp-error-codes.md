---
title: SNMP Error Codes (Snmp.h)
description: Microsoft implements the following SNMP error codes that are defined by the SNMPv2C specification.
ms.assetid: 7e7e2bc0-a058-4853-b736-1946e64a0c4a
topic_type:
- apiref
api_name:
- SNMP_ERRORSTATUS_NOERROR
- SNMP_ERRORSTATUS_TOOBIG
- SNMP_ERRORSTATUS_NOSUCHNAME
- SNMP_ERRORSTATUS_BADVALUE
- SNMP_ERRORSTATUS_READONLY
- SNMP_ERRORSTATUS_GENERR
- SNMP_ERRORSTATUS_NOACCESS
- SNMP_ERRORSTATUS_WRONGTYPE
- SNMP_ERRORSTATUS_WRONGLENGTH
- SNMP_ERRORSTATUS_WRONGENCODING
- SNMP_ERRORSTATUS_WRONGVALUE
- SNMP_ERRORSTATUS_NOCREATION
- SNMP_ERRORSTATUS_INCONSISTENTVALUE
- SNMP_ERRORSTATUS_RESOURCEUNAVAILABLE
- SNMP_ERRORSTATUS_COMMITFAILED
- SNMP_ERRORSTATUS_UNDOFAILED
- SNMP_ERRORSTATUS_AUTHORIZATIONERROR
- SNMP_ERRORSTATUS_NOTWRITABLE
- SNMP_ERRORSTATUS_INCONSISTENTNAME
api_location:
- Snmp.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# SNMP Error Codes

\[SNMP is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use [Windows Remote Management](/windows/desktop/WinRM/portal), which is the Microsoft implementation of WS-Man.\]

Microsoft implements the following SNMP error codes that are defined by the SNMPv2C specification.



| Constant/value                                                                                                                                                                                                                                                                              | Description                                                                                                                                                    |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SNMP_ERRORSTATUS_NOERROR"></span><span id="snmp_errorstatus_noerror"></span><dl> <dt>**SNMP\_ERRORSTATUS\_NOERROR**</dt> <dt>0</dt> </dl>                                      | The agent reports that no errors occurred during transmission.<br/>                                                                                      |
| <span id="SNMP_ERRORSTATUS_TOOBIG"></span><span id="snmp_errorstatus_toobig"></span><dl> <dt>**SNMP\_ERRORSTATUS\_TOOBIG**</dt> <dt>1</dt> </dl>                                         | The agent could not place the results of the requested SNMP operation in a single SNMP message.<br/>                                                     |
| <span id="SNMP_ERRORSTATUS_NOSUCHNAME"></span><span id="snmp_errorstatus_nosuchname"></span><dl> <dt>**SNMP\_ERRORSTATUS\_NOSUCHNAME**</dt> <dt>2</dt> </dl>                             | The requested SNMP operation identified an unknown variable.<br/>                                                                                        |
| <span id="SNMP_ERRORSTATUS_BADVALUE"></span><span id="snmp_errorstatus_badvalue"></span><dl> <dt>**SNMP\_ERRORSTATUS\_BADVALUE**</dt> <dt>3</dt> </dl>                                   | The requested SNMP operation tried to change a variable but it specified either a syntax or value error.<br/>                                            |
| <span id="SNMP_ERRORSTATUS_READONLY"></span><span id="snmp_errorstatus_readonly"></span><dl> <dt>**SNMP\_ERRORSTATUS\_READONLY**</dt> <dt>4</dt> </dl>                                   | The requested SNMP operation tried to change a variable that was not allowed to change, according to the community profile of the variable.<br/>         |
| <span id="SNMP_ERRORSTATUS_GENERR"></span><span id="snmp_errorstatus_generr"></span><dl> <dt>**SNMP\_ERRORSTATUS\_GENERR**</dt> <dt>5</dt> </dl>                                         | An error other than one of those listed here occurred during the requested SNMP operation.<br/>                                                          |
| <span id="SNMP_ERRORSTATUS_NOACCESS"></span><span id="snmp_errorstatus_noaccess"></span><dl> <dt>**SNMP\_ERRORSTATUS\_NOACCESS**</dt> <dt>6</dt> </dl>                                   | The specified SNMP variable is not accessible.<br/>                                                                                                      |
| <span id="SNMP_ERRORSTATUS_WRONGTYPE"></span><span id="snmp_errorstatus_wrongtype"></span><dl> <dt>**SNMP\_ERRORSTATUS\_WRONGTYPE**</dt> <dt>7</dt> </dl>                                | The value specifies a type that is inconsistent with the type required for the variable.<br/>                                                            |
| <span id="SNMP_ERRORSTATUS_WRONGLENGTH"></span><span id="snmp_errorstatus_wronglength"></span><dl> <dt>**SNMP\_ERRORSTATUS\_WRONGLENGTH**</dt> <dt>8</dt> </dl>                          | The value specifies a length that is inconsistent with the length required for the variable.<br/>                                                        |
| <span id="SNMP_ERRORSTATUS_WRONGENCODING"></span><span id="snmp_errorstatus_wrongencoding"></span><dl> <dt>**SNMP\_ERRORSTATUS\_WRONGENCODING**</dt> <dt>9</dt> </dl>                    | The value contains an Abstract Syntax Notation One (ASN.1) encoding that is inconsistent with the ASN.1 tag of the field.<br/>                           |
| <span id="SNMP_ERRORSTATUS_WRONGVALUE"></span><span id="snmp_errorstatus_wrongvalue"></span><dl> <dt>**SNMP\_ERRORSTATUS\_WRONGVALUE**</dt> <dt>10</dt> </dl>                            | The value cannot be assigned to the variable.<br/>                                                                                                       |
| <span id="SNMP_ERRORSTATUS_NOCREATION"></span><span id="snmp_errorstatus_nocreation"></span><dl> <dt>**SNMP\_ERRORSTATUS\_NOCREATION**</dt> <dt>11</dt> </dl>                            | The variable does not exist, and the agent cannot create it.<br/>                                                                                        |
| <span id="SNMP_ERRORSTATUS_INCONSISTENTVALUE"></span><span id="snmp_errorstatus_inconsistentvalue"></span><dl> <dt>**SNMP\_ERRORSTATUS\_INCONSISTENTVALUE**</dt> <dt>12</dt> </dl>       | The value is inconsistent with values of other managed objects.<br/>                                                                                     |
| <span id="SNMP_ERRORSTATUS_RESOURCEUNAVAILABLE"></span><span id="snmp_errorstatus_resourceunavailable"></span><dl> <dt>**SNMP\_ERRORSTATUS\_RESOURCEUNAVAILABLE**</dt> <dt>13</dt> </dl> | Assigning the value to the variable requires allocation of resources that are currently unavailable.<br/>                                                |
| <span id="SNMP_ERRORSTATUS_COMMITFAILED"></span><span id="snmp_errorstatus_commitfailed"></span><dl> <dt>**SNMP\_ERRORSTATUS\_COMMITFAILED**</dt> <dt>14</dt> </dl>                      | No validation errors occurred, but no variables were updated.<br/>                                                                                       |
| <span id="SNMP_ERRORSTATUS_UNDOFAILED"></span><span id="snmp_errorstatus_undofailed"></span><dl> <dt>**SNMP\_ERRORSTATUS\_UNDOFAILED**</dt> <dt>15</dt> </dl>                            | No validation errors occurred. Some variables were updated because it was not possible to undo their assignment.<br/>                                    |
| <span id="SNMP_ERRORSTATUS_AUTHORIZATIONERROR"></span><span id="snmp_errorstatus_authorizationerror"></span><dl> <dt>**SNMP\_ERRORSTATUS\_AUTHORIZATIONERROR**</dt> <dt>16</dt> </dl>    | An authorization error occurred.<br/>                                                                                                                    |
| <span id="SNMP_ERRORSTATUS_NOTWRITABLE"></span><span id="snmp_errorstatus_notwritable"></span><dl> <dt>**SNMP\_ERRORSTATUS\_NOTWRITABLE**</dt> <dt>17</dt> </dl>                         | The variable exists but the agent cannot modify it.<br/>                                                                                                 |
| <span id="SNMP_ERRORSTATUS_INCONSISTENTNAME"></span><span id="snmp_errorstatus_inconsistentname"></span><dl> <dt>**SNMP\_ERRORSTATUS\_INCONSISTENTNAME**</dt> <dt>18</dt> </dl>          | The variable does not exist; the agent cannot create it because the named object instance is inconsistent with the values of other managed objects.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                        |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                              |
| Header<br/>                   | <dl> <dt>Snmp.h</dt> </dl> |



## See also

<dl> <dt>

[Simple Network Management Protocol (SNMP) Overview](simple-network-management-protocol-snmp-.md)
</dt> <dt>

[SNMP Reference](snmp-reference.md)
</dt> </dl>

 


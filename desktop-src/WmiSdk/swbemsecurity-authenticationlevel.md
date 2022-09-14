---
description: The AuthenticationLevel property is an integer that defines the COM Authentication level that is assigned to this object.
ms.assetid: 96c2e6a5-a91f-469d-bdd1-eaa20b176158
ms.tgt_platform: multiple
title: SWbemSecurity.AuthenticationLevel property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemSecurity.AuthenticationLevel
- ISWbemSecurity.AuthenticationLevel
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemSecurity.AuthenticationLevel property

The **AuthenticationLevel** property is an integer that defines the COM Authentication level that is assigned to this object. This setting determines how you protect information sent from WMI. For more information about authentication levels, see [Setting Client\_Application\_Process Security](setting-client-application-process-security.md). In general, it is not necessary to set the authentication level when making WMI API calls. If you do not set this property, the default COM Authentication level for your system is used.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

This property is read/write.

## Syntax


```VB
SWbemSecurity.AuthenticationLevel As Integer
```



## Property value

## Remarks

The authenticationLevel setting enables you to request the level of DCOM authentication and privacy to be used throughout a connection. Settings range from no authentication to per-packet encrypted authentication.



| Value        | Description                                                                                                                                                                                                                                                                                                            |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| None         | Does not use any authentication. All security settings are ignored.<br/>                                                                                                                                                                                                                                         |
| Default      | Uses a standard security negotiation to select an authentication level. This is the recommended setting because the client involved in the transaction will be negotiated to the authentication level specified by the server.<br/> DCOM will not select the value None during a negotiation session.<br/> |
| Connect      | Authenticates the credentials of the client only when the client tries to connect to the server. After a connection has been made, no additional authentication checks take place.<br/>                                                                                                                          |
| Call         | Authenticates the credentials of the client only at the beginning of each call, when the server receives the request. The packet headers are signed, but the data packets exchanged between the client and the server are neither signed nor encrypted.<br/>                                                     |
| Pkt          | Authenticates that all data packets are received from the expected client. Similar to Call; packet headers are signed but not encrypted. Packets themselves are neither signed nor encrypted.<br/>                                                                                                               |
| PktIntegrity | Authenticates and verifies that none of the data packets transferred between the client and the server have been modified. Every data packet is signed, ensuring that the packets have not been modified during transit. None of the data packets are encrypted.<br/>                                            |
| PktPrivacy   | Authenticates all previous impersonation levels and signs and encrypts each data packet. This ensures that all communication between the client and the server is confidential.<br/>                                                                                                                             |



 

You can set the authentication level of the [**SWbemServices**](swbemservices.md), [**SWbemObject**](swbemobject.md), [**SWbemObjectSet**](swbemobjectset.md), [**SWbemObjectPath**](swbemobjectpath.md), and [**SwbemLocator**](swbemlocator.md) objects by setting the **AuthenticationLevel** property to the desired value.

The following example shows how to set the authentication level for an **SwbemObject** object.


```VB
objinstance.Security_.AuthenticationLevel = wbemAuthenticationLevelPkt
```



You can also specify authentication levels as part of a moniker. The following example sets the authentication level and the impersonation level, and retrieves an instance of [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk).


```VB
Set objinst = GetObject("WinMgmts:{impersonationLevel=impersonate,authenticationLevel=pktPrivacy}!root/cimv2:Win32_LogicalDisk='c:'")
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemSecurity<br/>                                                         |
| IID<br/>                      | IID\_ISWbemSecurity<br/>                                                          |



## See also

<dl> <dt>

[Setting Client\_Application\_Process Security](setting-client-application-process-security.md)
</dt> <dt>

[**WbemAuthenticationLevelEnum**](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemauthenticationlevelenum)
</dt> <dt>

[**SWbemSecurity**](swbemsecurity.md)
</dt> </dl>

 


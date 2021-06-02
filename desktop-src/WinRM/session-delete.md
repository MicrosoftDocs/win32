---
title: Session.Delete method (WSManDisp.h)
description: Deletes the resource specified in the resource URI.
ms.assetid: 8803d35d-674c-483d-866b-37129102c7ce
ms.tgt_platform: multiple
keywords:
- Delete method Windows Remote Management
- Delete method Windows Remote Management , Session object
- Session object Windows Remote Management , Delete method
topic_type:
- apiref
api_name:
- Session.Delete
api_location:
- WSMAuto.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Session.Delete method

Deletes the resource specified in the resource URI.

## Syntax


```VB
Session.Delete( _
  ByVal resourceUri, _
  [ ByVal flags ] _
)
```



## Parameters

<dl> <dt>

*resourceUri* \[in\]
</dt> <dd>

The URI of the resource to be deleted. You can also use a [**ResourceLocator**](resourcelocator.md) object to specify the resource.

</dd> <dt>

*flags* \[in, optional\]
</dt> <dd>

Reserved for future use. Must be set to 0.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The following syntax is used to call this method.


```VB
session.Delete("<resourceUri>")
```



## Examples

The following VBScript code example deletes the listeners configured for HTTP transport.


```VB
Set objWsman = CreateObject( "WSMan.Automation" )
Set objSession = objWsman.CreateSession
strResource = "http://schemas.microsoft.com/wbem/wsman/1/" &_
  "config/Listener?Address=*+Transport=HTTP"
objSession.Delete(strResource)
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Header<br/>                   | <dl> <dt>WSManDisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>WSManDisp.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>WSManDisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WSMAuto.dll</dt> </dl>   |



## See also

<dl> <dt>

[**Session**](session.md)
</dt> </dl>

 

 






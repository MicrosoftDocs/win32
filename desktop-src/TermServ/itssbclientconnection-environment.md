---
title: ITsSbClientConnection Environment property
description: Retrieves an object that contains information about the environment that hosts the target computer.
ms.assetid: 97fe4851-96a9-4b23-8ad7-f42b87c655d0
ms.tgt_platform: multiple
keywords:
- Environment property Remote Desktop Services
- Environment property Remote Desktop Services , ITsSbClientConnection interface
- ITsSbClientConnection interface Remote Desktop Services , Environment property
topic_type:
- apiref
api_name:
- ITsSbClientConnection.Environment
- ITsSbClientConnection.get_Environment
api_location:
- Sbtsv.idl
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ITsSbClientConnection::Environment property

Retrieves an object that contains information about the environment that hosts the target computer. For example, in a virtual desktop scenario, this object would contain information about the computer that hosts the virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_Environment(
  [out, retval] ITsSbEnvironment **ppEnvironment
);
```



## Property value

A pointer to a pointer to an [**ITsSbEnvironment**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbenvironment) environment object.

## Error codes

If the method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** value that indicates the error. Possible values include, but are not limited to, those in the following list.

<dl> <dt>

E\_POINTER
</dt> <dd>

The environment was not found.

</dd> </dl>

## Remarks

An orchestration plug-in can call this method to retrieve environment information about a target virtual machine.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                       |
| IDL<br/>                      | <dl> <dt>Sbtsv.idl</dt> </dl> |



## See also

<dl> <dt>

[**ITsSbClientConnection**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbclientconnection)
</dt> </dl>

 

 






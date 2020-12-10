---
title: ITsSbEnvironment Name property
description: Retrieves a value that indicates the name of the environment that hosts the target computer.
ms.assetid: 8104bdae-f445-425b-b326-cc3333839d29
ms.tgt_platform: multiple
keywords:
- Name property Remote Desktop Services
- Name property Remote Desktop Services , ITsSbEnvironment interface
- ITsSbEnvironment interface Remote Desktop Services , Name property
topic_type:
- apiref
api_name:
- ITsSbEnvironment.Name
- ITsSbEnvironment.get_Name
api_location:
- Sbtsv.idl
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ITsSbEnvironment::Name property

Retrieves a value that indicates the name of the environment that hosts the target computer.

This property is read-only.

## Syntax


```C++
HRESULT get_Name(
  [out, retval] BSTR *pVal
);
```



## Property value

A pointer to a **BSTR** variable that contains the name of the environment.

## Remarks

This method returns a string that is not directly used by Remote Desktop Connection Broker (RD Connection Broker). RD Connection Broker passes this string to resource plug-ins.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                       |
| IDL<br/>                      | <dl> <dt>Sbtsv.idl</dt> </dl> |



## See also

<dl> <dt>

[**ITsSbEnvironment**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbenvironment)
</dt> </dl>

 

 






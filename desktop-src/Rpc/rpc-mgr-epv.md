---
title: RPC_MGR_EPV (Rpcdce.h)
description: The data type RPC\_MGR\_EPV defines a manager entry-point vector.
ms.assetid: 396e76de-065f-471e-ade9-34770b16a958
keywords:
- RPC_MGR_EPV RPC
topic_type:
- apiref
api_name:
- RPC_MGR_EPV
api_location:
- Rpcdce.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# RPC\_MGR\_EPV

The data type **RPC\_MGR\_EPV** defines a manager entry-point vector.

``` syntax
typedef void RPC_MGR_EPV;
typedef _if-name_SERVER-EPV {
  return-type (* Functionname)  (param-list);
...  //one entry for each function in IDL file
} if-name_SERVER_EPV:
```

## Members

<dl> <dt>

<span id="if-name"></span><span id="IF-NAME"></span>**if-name**
</dt> <dd>

Specifies the name of the interface

</dd> <dt>

<span id="return-type"></span><span id="RETURN-TYPE"></span>**return-type**
</dt> <dd>

Specifies the type returned by the function **Functionname** indicated in the IDL file.

</dd> <dt>

<span id="Functionname"></span><span id="functionname"></span><span id="FUNCTIONNAME"></span>**Functionname**
</dt> <dd>

Specifies the name of the function indicated in the IDL file.

</dd> <dt>

<span id="param-list"></span><span id="PARAM-LIST"></span>**param-list**
</dt> <dd>

Specifies the parameters indicated for the function **Functionname** in the IDL file.

</dd> </dl>

## Remarks

The manager entry-point vector (EPV) is an array of function pointers. The array contains pointers to the implementations of the functions specified in the IDL file. The number of elements in the array is set to the number of functions specified in the IDL file. An application can also have multiple EPVs, representing multiple implementations of the functions specified in the interface.

The MIDL compiler generates a default **EPV** data type named *if-name***\_SERVER\_EPV**, where *if-name* specifies the interface identifier in the IDL file. The MIDL compiler initializes this default **EPV** to contain function pointers for each of the procedures specified in the IDL file.

When the server offers multiple implementations of the same interface, the server application must declare and initialize one variable of type *if-name***\_SERVER\_EPV** for each implementation of the interface. Each **EPV** must contain one entry point (function pointer) for each procedure defined in the IDL file.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                |
| Header<br/>                   | <dl> <dt>Rpcdce.h (include Rpc.h)</dt> </dl> |



## See also

<dl> <dt>

[**RpcServerRegisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif)
</dt> <dt>

[**RpcServerRegisterIf2**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif2)
</dt> <dt>

[**RpcServerRegisterIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterifex)
</dt> <dt>

[**RpcServerUnregisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverunregisterif)
</dt> <dt>

[**RpcServerUnregisterIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverunregisterifex)
</dt> </dl>

 

 






---
title: ORPC_DBG_BUFFER structure
description: The ORPC\_DBG\_BUFFER structure is the buffer format used to marshalled RPC data to the methods of the IOrpcDebugNotify interface.
ms.assetid: 444cd3b8-bc7b-425d-9ccc-04fd6c7393b2
keywords:
- ORPC_DBG_BUFFER structure COM
- PORPC_DBG_BUFFER structure pointer COM
topic_type:
- apiref
api_name:
- ORPC_DBG_BUFFER
api_location:
- N/A
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ORPC\_DBG\_BUFFER structure

The **ORPC\_DBG\_BUFFER** structure is the buffer format used to marshalled RPC data to the methods of the [**IOrpcDebugNotify**](iorpcdebugnotify.md) interface.

## Syntax


```C++
typedef struct _ORPC_DBG_BUFFER {
  DWORD alwaysOrSometimes;
  BYTE  verMajor;
  BYTE  verMinor;
  DWORD cbRemaining;
  GUID  guidSemantic;
  union {
    BOOL   fStopOnOtherSide;
    USHORT wDebuggingOpCode;
    USHORT cExtent;
    BYTE   padding[2];
    struct {
      ULONG cb;
      GUID  guidExtent;
      BYTE  *rgbData;
    };
  };
} ORPC_DBG_BUFFER, *PORPC_DBG_BUFFER;
```



## Members

<dl> <dt>

**alwaysOrSometimes**
</dt> <dd>

A value that controls debugger spawning. **alwaysOrSometimes** can be one of the following values:



| Value                                                                                                                                                                                                                                                                   | Meaning                                                                                                                                                                                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="ORPC_DEBUG_ALWAYS"></span><span id="orpc_debug_always"></span><dl> <dt>**ORPC\_DEBUG\_ALWAYS**</dt> <dt>0x00000000</dt> </dl>                              | If set, COM will always raise the client or server notification on the receiver.<br/>                                                                                                                                                    |
| <span id="ORPC_DEBUG_IF_HOOK_ENABLED"></span><span id="orpc_debug_if_hook_enabled"></span><dl> <dt>**ORPC\_DEBUG\_IF\_HOOK\_ENABLED**</dt> <dt>0x00000001</dt> </dl> | If set, COM will only raise the client or server notification on the receiver if COM debugging has been enabled by calling [**DllDebugObjectRPCHook**](dlldebugobjectrpchook.md) in that process with **fTrace** set to **TRUE**. <br/> |



 

</dd> <dt>

**verMajor**
</dt> <dd>

The major version number of the data format specification.

</dd> <dt>

**verMinor**
</dt> <dd>

The minor version number of the data format specification.

</dd> <dt>

**cbRemaining**
</dt> <dd>

The number of bytes, inclusive of **cbRemaining**, that follow in this structure.

</dd> <dt>

**guidSemantic**
</dt> <dd>

A GUID that determines which members of the union are present below. **guidSemantic** can take one of the following values:



| Value                                                                                                           | Meaning                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>9CADE560-8F43-101A-B07B-00DD01113F11</dt> </dl> | Determines if single stepping is to be performed by the debugger. Only the **fStopOnOtherSide** member of the union is present below.<br/>                                             |
| <dl> <dt>D62AEDFA-57EA-11ce-A964-00AA006C3706</dt> </dl> | Determines if RPC marshalled data and debugging opcodes are passed to the receiver. All of the members of the union are present below with the exception of **fStopOnOtherSide**.<br/> |



 

</dd> <dt>

**fStopOnOtherSide**
</dt> <dd>

If **TRUE**, single stepping is performed by the debugger and it should step out of the server and continue execution once the other side is reached. Otherwise, single stepping is not performed and debugger execution stops on the other side.

</dd> <dt>

**wDebuggingOpCode**
</dt> <dd>

A value that allows for one of a series of operations to be specified. **wDebuggingOpCode** can take one of the following values:



| Value                                                                             | Meaning                                                                                              |
|-----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <dl> <dt>0x0000</dt> </dl> | No operation.<br/>                                                                             |
| <dl> <dt>0x0001</dt> </dl> | If set, single step semantics are identical to **fStopOnOtherSide** when set to **TRUE**.<br/> |



 

</dd> <dt>

**cExtent**
</dt> <dd>

Padding. Do not use.

</dd> <dt>

**padding**
</dt> <dd>

Padding. Do not use.

</dd> <dt>

**cb**
</dt> <dd>

The size, in bytes of the data in **rgbData**.

</dd> <dt>

**guidExtent**
</dt> <dd>

A **GUID** that determines the type of data in **rgbData**. **guidExtent** can take one of the following values:



| Value                                                                                                           | Meaning                                                   |
|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>53199051-57EB-11ce-A964-00AA006C3706</dt> </dl> | **rgbData** is a marshalled interface pointer.<br/> |



 

</dd> <dt>

**rgbData**
</dt> <dd>

A **BYTE** buffer used to pass RPC marshalled COM data between the client and server debuggers. The contents of **rgbData** are determined by the **GUID** in **guidExtent**.



| guidExtent Value                     | rgbData contents                                                                                                                                                                                                                                    |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 53199051-57EB-11ce-A964-00AA006C3706 | A marshalled interface pointer that results from calling [**CoMarshalInterface**](/windows/desktop/api/combaseapi/nf-combaseapi-comarshalinterface). The marshalled pointer is converted into its corresponding interface pointer using [**CoUnmarshalInterface**](/windows/desktop/api/combaseapi/nf-combaseapi-counmarshalinterface). |



 

</dd> </dl>

## Remarks

This members of this structure have 1-byte alignment and are always transmitted in little-endian byte order.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                     |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                           |
| Header<br/>                   | <dl> <dt>N/A</dt> </dl> |



## See also

<dl> <dt>

[**ORPC\_DBG\_ALL**](orpc-dbg-all.md)
</dt> <dt>

[**ORPC\_INIT\_ARGS**](orpc-init-args.md)
</dt> <dt>

[**DllDebugObjectRPCHook**](dlldebugobjectrpchook.md)
</dt> <dt>

[**IOrpcDebugNotify**](iorpcdebugnotify.md)
</dt> </dl>

 

 






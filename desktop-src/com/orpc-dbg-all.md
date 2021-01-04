---
title: ORPC_DBG_ALL structure
description: The ORPC\_DBG\_ALL structure is used to pass parameters to the methods of the IOrpcDebugNotify interface.
ms.assetid: 05371beb-9202-40a6-96d2-4b91497e2ee9
keywords:
- ORPC_DBG_ALL structure COM
- LPORPC_DBG_ALL structure pointer COM
topic_type:
- apiref
api_name:
- ORPC_DBG_ALL
api_location:
- N/A
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ORPC\_DBG\_ALL structure

The **ORPC\_DBG\_ALL** structure is used to pass parameters to the methods of the [**IOrpcDebugNotify**](iorpcdebugnotify.md) interface.

> [!Note]  
> Each method of the [**IOrpcDebugNotify**](iorpcdebugnotify.md) interface uses a different combination of the members below. If a member is not indicated as used by a method, it is undefined when passed to that method.

 

## Syntax


```C++
typedef struct ORPC_DBG_ALL {
  BYTE              *pSignature;
  RPCOLEMESSAGE     *pMessage;
  const IID         *refiid;
  IRpcChannelBuffer *pChannel;
  IUnknown          *pUnkProxyMgr;
  void              *pInterface;
  IUnknown          *pUnkObject;
  HRESULT           hresult;
  void              *pvBuffer;
  ULONG             *cbBuffer;
  ULONG             *lpcbBuffer;
  void              *reserved;
} ORPC_DBG_ALL, *LPORPC_DBG_ALL;
```



## Members

<dl> <dt>

**pSignature**
</dt> <dd>

A pointer to a **BYTE** buffer that contains:

-   First four bytes: the ASCII characters "MARB" in increasing memory order.
-   Next 16 bytes: A **GUID** that identifies the notification being called. It contains one of the following:
    1.  [**ClientGetBufferSize**](iorpcdebugnotify-clientgetbuffersize.md): 9ED14F80-9673-101A-B07B-00DD01113F11
    2.  [**ClientFillBuffer**](iorpcdebugnotify-clientfillbuffer.md):DA45F3E0-9673-101A-B07B-00DD01113F11
    3.  [**ClientNotify**](iorpcdebugnotify-clientnotify.md):4F60E540-9674-101A-B07B-00DD01113F11
    4.  [**ServerNotify**](iorpcdebugnotify-servernotify.md):1084FA00-9674-101A-B07B-00DD01113F11
    5.  [**ServerGetBufferSize**](iorpcdebugnotify-servergetbuffersize.md):22080240-9674-101A-B07B-00DD01113F11
    6.  [**ServerFillBuffer**](iorpcdebugnotify-serverfillbuffer.md):2FC09500-9674-101A-B07B-00DD01113F11
-   Next four-bytes: Reserved for future use.

> [!Note]
>
> Used by all methods of the [**IOrpcDebugNotify**](iorpcdebugnotify.md) interface.

 

</dd> <dt>

**pMessage**
</dt> <dd>

A pointer to an [**RPCOLEMESSAGE**](/windows/win32/api/objidlbase/ns-objidlbase-rpcolemessage) structure that contains RPC data marshalling information.

> [!Note]
>
> Used by the [**ClientFillBuffer**](iorpcdebugnotify-clientfillbuffer.md), [**ClientGetBufferSize**](iorpcdebugnotify-clientgetbuffersize.md), [**ClientNotify**](iorpcdebugnotify-clientnotify.md), [**ServerFillBuffer**](iorpcdebugnotify-serverfillbuffer.md), [**ServerGetBufferSize**](iorpcdebugnotify-servergetbuffersize.md), and [**ServerNotify**](iorpcdebugnotify-servernotify.md) methods.

 

</dd> <dt>

**refiid**
</dt> <dd>

A pointer to the IID of the [**IOrpcDebugNotify**](iorpcdebugnotify.md) interface.

> [!Note]
>
> Used by the [**ClientFillBuffer**](iorpcdebugnotify-clientfillbuffer.md), [**ClientGetBufferSize**](iorpcdebugnotify-clientgetbuffersize.md), [**ClientNotify**](iorpcdebugnotify-clientnotify.md), [**ServerFillBuffer**](iorpcdebugnotify-serverfillbuffer.md), [**ServerGetBufferSize**](iorpcdebugnotify-servergetbuffersize.md), and [**ServerNotify**](iorpcdebugnotify-servernotify.md) methods.

 

</dd> <dt>

**pChannel**
</dt> <dd>

A pointer to the [**IRpcChannelBuffer**](/windows/win32/api/objidlbase/nn-objidlbase-irpcchannelbuffer) interface of the COM RPC channel implementation on the server.

> [!Note]
>
> Used by the [**ServerFillBuffer**](iorpcdebugnotify-serverfillbuffer.md), [**ServerGetBufferSize**](iorpcdebugnotify-servergetbuffersize.md), and [**ServerNotify**](iorpcdebugnotify-servernotify.md) methods.

 

</dd> <dt>

**pUnkProxyMgr**
</dt> <dd>

A pointer to the [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) interface of the object involved in this debugger invocation. May be **NULL**, however, this reduces debugger functionality.

> [!Note]
>
> Used by the [**ClientFillBuffer**](iorpcdebugnotify-clientfillbuffer.md), [**ClientGetBufferSize**](iorpcdebugnotify-clientgetbuffersize.md), and [**ClientNotify**](iorpcdebugnotify-clientnotify.md) methods.

 

</dd> <dt>

**pInterface**
</dt> <dd>

A pointer to the COM interface of the method that will be invoked by this RPC. Must not be **NULL**.

> [!Note]
>
> Used by the [**ServerFillBuffer**](iorpcdebugnotify-serverfillbuffer.md), [**ServerGetBufferSize**](iorpcdebugnotify-servergetbuffersize.md), and [**ServerNotify**](iorpcdebugnotify-servernotify.md) methods.

 

</dd> <dt>

**pUnkObject**
</dt> <dd>

Must be **NULL**.

> [!Note]
>
> Used by the [**ServerFillBuffer**](iorpcdebugnotify-serverfillbuffer.md), [**ServerGetBufferSize**](iorpcdebugnotify-servergetbuffersize.md), and [**ServerNotify**](iorpcdebugnotify-servernotify.md) methods.

 

</dd> <dt>

**hresult**
</dt> <dd>

This member's purpose changes for each of the notifications below:

[**ClientGetBufferSize**](iorpcdebugnotify-clientgetbuffersize.md): the number of bytes the client debugger will transmit to the server debugger. If zero, no information need be transmitted.

[**ClientNotify**](iorpcdebugnotify-clientnotify.md): the **HRESULT** of the last RPC.

[**ServerGetBufferSize**](iorpcdebugnotify-servergetbuffersize.md): the number of bytes the client debugger will transmit to the server debugger. If zero, no information need be transmitted.

> [!Note]
>
> Used by the [**ClientGetBufferSize**](iorpcdebugnotify-clientgetbuffersize.md), [**ClientNotify**](iorpcdebugnotify-clientnotify.md), and [**ServerGetBufferSize**](iorpcdebugnotify-servergetbuffersize.md) methods.

 

</dd> <dt>

**pvBuffer**
</dt> <dd>

A pointer to an [**ORPC\_DBG\_BUFFER**](orpc-dbg-buffer.md) structure that contains the RPC marshalled debug information. Is undefined if **cbBuffer** is zero.

> [!Note]
>
> Used by the [**ClientFillBuffer**](iorpcdebugnotify-clientfillbuffer.md), [**ClientNotify**](iorpcdebugnotify-clientnotify.md), [**ServerFillBuffer**](iorpcdebugnotify-serverfillbuffer.md), and [**ServerNotify**](iorpcdebugnotify-servernotify.md) methods.

 

</dd> <dt>

**cbBuffer**
</dt> <dd>

The length, in bytes, of the data pointed to by **pvBuffer**.

> [!Note]
>
> Used by the [**ClientFillBuffer**](iorpcdebugnotify-clientfillbuffer.md), [**ClientNotify**](iorpcdebugnotify-clientnotify.md), [**ServerFillBuffer**](iorpcdebugnotify-serverfillbuffer.md), and [**ServerNotify**](iorpcdebugnotify-servernotify.md) methods.

 

</dd> <dt>

**lpcbBuffer**
</dt> <dd>

The number of bytes the client debugger will transmit to the server debugger. If zero, no information need be transmitted. This value supersedes the value returned in **hresult**.

> [!Note]
>
> Used by the [**ClientFillBuffer**](iorpcdebugnotify-clientfillbuffer.md), [**ClientGetBufferSize**](iorpcdebugnotify-clientgetbuffersize.md) methods.

 

</dd> <dt>

**reserved**
</dt> <dd>

Reserved. Do not use.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                     |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                           |
| Header<br/>                   | <dl> <dt>N/A</dt> </dl> |



## See also

<dl> <dt>

[**ORPC\_DBG\_BUFFER**](orpc-dbg-buffer.md)
</dt> <dt>

[**ORPC\_INIT\_ARGS**](orpc-init-args.md)
</dt> <dt>

[**DllDebugObjectRPCHook**](dlldebugobjectrpchook.md)
</dt> <dt>

[**IOrpcDebugNotify**](iorpcdebugnotify.md)
</dt> </dl>

 


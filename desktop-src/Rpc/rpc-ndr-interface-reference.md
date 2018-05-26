---
title: RPC NDR Interface Reference
description: Microsoft RPC NDR currently supports the following functions and structures
ms.assetid: 2EBB2DD6-60DD-4C9F-9F79-231383B28517
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RPC NDR Interface Reference

Microsoft RPC NDR currently supports the following functions and structures:

-   [**CStdStubBuffer\_AddRef**](/windows/win32/Rpcproxy/nf-rpcproxy-cstdstubbuffer_addref?branch=master)
-   [**CStdStubBuffer\_Connect**](/windows/win32/Rpcproxy/nf-rpcproxy-cstdstubbuffer_connect?branch=master)
-   [**CStdStubBuffer\_CountRefs**](/windows/win32/Rpcproxy/nf-rpcproxy-cstdstubbuffer_countrefs?branch=master)
-   [**CStdStubBuffer\_DebugServerQueryInterface**](/windows/win32/Rpcproxy/nf-rpcproxy-cstdstubbuffer_debugserverqueryinterface?branch=master)
-   [**CStdStubBuffer\_DebugServerRelease**](/windows/win32/Rpcproxy/nf-rpcproxy-cstdstubbuffer_debugserverrelease?branch=master)
-   [**CStdStubBuffer\_Disconnect**](/windows/win32/Rpcproxy/nf-rpcproxy-cstdstubbuffer_disconnect?branch=master)
-   [**CStdStubBuffer\_Invoke**](/windows/win32/Rpcproxy/nf-rpcproxy-cstdstubbuffer_invoke?branch=master)
-   [**CStdStubBuffer\_IsIIDSupported**](/windows/win32/RpcProxy/nf-rpcproxy-cstdstubbuffer_isiidsupported?branch=master)
-   [**CStdStubBuffer\_QueryInterface**](/windows/win32/Rpcproxy/nf-rpcproxy-cstdstubbuffer_queryinterface?branch=master)
-   [**IUnknown\_AddRef\_Proxy**](/windows/win32/unknwnbase/nf-unknwnbase-iunknown_addref_proxy?branch=master)
-   [**IUnknown\_QueryInterface\_Proxy**](/windows/win32/unknwnbase/nf-unknwnbase-iunknown_queryinterface_proxy?branch=master)
-   [**IUnknown\_Release\_Proxy**](/windows/win32/unknwnbase/nf-unknwnbase-iunknown_queryinterface_proxy?branch=master)
-   [**NdrAsyncClientCall**](/windows/win32/Rpcndr/nf-rpcndr-ndrasyncclientcall?branch=master)
-   [**NdrClearOutParameters**](/windows/win32/Rpcndr/nf-rpcndr-ndrclearoutparameters?branch=master)
-   [**NdrClientCall**](/windows/win32/Rpcndr/nf-rpcndr-ndrclientcall?branch=master)
-   [**NdrClientCall2**](/windows/win32/Rpcndr/nf-rpcndr-ndrclientcall2?branch=master)
-   [**NdrConformantArrayUnmarshall**](/windows/win32/Rpcndr/nf-rpcndr-ndrconformantarrayunmarshall?branch=master)
-   [**NdrConformantStringBufferSize**](/windows/win32/Rpcndr/nf-rpcndr-ndrconformantstringbuffersize?branch=master)
-   [**NdrConformantStringMarshall**](/windows/win32/Rpcndr/nf-rpcndr-ndrconformantstringmarshall?branch=master)
-   [**NdrConformantStringUnmarshall**](/windows/win32/Rpcndr/nf-rpcndr-ndrconformantstringunmarshall?branch=master)
-   [**NdrContextHandleInitialize**](/windows/win32/Rpcndr/nf-rpcndr-ndrcontexthandleinitialize?branch=master)
-   [**NdrContextHandleSize**](/windows/win32/Rpcndr/nf-rpcndr-ndrcontexthandlesize?branch=master)
-   [**NdrContextHandleMemorySize**](/windows/win32/Rpcndr/nf-rpcndr-ndrcontexthandlememorysize?branch=master)
-   [**NdrConvert**](/windows/win32/Rpcndr/nf-rpcndr-ndrconvert?branch=master)
-   [**NdrCStdStubBuffer\_Release**](ndrcstdstubbuffer-release.md)
-   [**NdrCStdStubBuffer2\_Release**](ndrcstdstubbuffer2-release.md)
-   [**NdrDllCanUnloadNow**](/windows/win32/Rpcproxy/nf-rpcproxy-ndrdllcanunloadnow?branch=master)
-   [**NdrDllGetClassObject**](/windows/win32/Rpcproxy/nf-rpcproxy-ndrdllgetclassobject?branch=master)
-   [**NdrDllRegisterProxy**](/windows/win32/Rpcproxy/nf-rpcproxy-ndrdllregisterproxy?branch=master)
-   [**NdrDllUnregisterProxy**](/windows/win32/Rpcproxy/nf-rpcproxy-ndrdllunregisterproxy?branch=master)
-   [**NdrGetUserMarshalInfo**](/windows/win32/Rpcndr/nf-rpcndr-ndrgetusermarshalinfo?branch=master)
-   [**NdrInterfacePointerBufferSize**](/windows/win32/Rpcndr/nf-rpcndr-ndrinterfacepointerbuffersize?branch=master)
-   [**NdrInterfacePointerFree**](/windows/win32/Rpcndr/nf-rpcndr-ndrinterfacepointerfree?branch=master)
-   [**NdrInterfacePointerMarshall**](/windows/win32/Rpcndr/nf-rpcndr-ndrinterfacepointermarshall?branch=master)
-   [**NdrInterfacePointerUnmarshall**](/windows/win32/Rpcndr/nf-rpcndr-ndrinterfacepointerunmarshall?branch=master)
-   [**NdrOleAllocate**](/windows/win32/Rpcndr/nf-rpcndr-ndroleallocate?branch=master)
-   [**NdrOleFree**](/windows/win32/Rpcndr/nf-rpcndr-ndrolefree?branch=master)
-   [**NdrPointerBufferSize**](/windows/win32/Rpcndr/nf-rpcndr-ndrpointerbuffersize?branch=master)
-   [**NdrPointerFree**](/windows/win32/Rpcndr/nf-rpcndr-ndrpointerfree?branch=master)
-   [**NdrPointerMarshall**](/windows/win32/Rpcndr/nf-rpcndr-ndrpointermarshall?branch=master)
-   [**NdrPointerUnmarshall**](/windows/win32/Rpcndr/nf-rpcndr-ndrpointerunmarshall?branch=master)
-   [**NdrProxyErrorHandler**](/windows/win32/Rpcproxy/nf-rpcproxy-ndrproxyerrorhandler?branch=master)
-   [**NdrProxyFreeBuffer**](/windows/win32/Rpcproxy/nf-rpcproxy-ndrproxyfreebuffer?branch=master)
-   [**NdrProxyGetBuffer**](/windows/win32/Rpcproxy/nf-rpcproxy-ndrproxygetbuffer?branch=master)
-   [**NdrProxyInitialize**](/windows/win32/Rpcproxy/nf-rpcproxy-ndrproxyinitialize?branch=master)
-   [**NdrProxySendReceive**](/windows/win32/Rpcproxy/nf-rpcproxy-ndrproxysendreceive?branch=master)
-   [**NdrSimpleTypeMarshall**](/windows/win32/Rpcndr/nf-rpcndr-ndrsimpletypemarshall?branch=master)
-   [**NdrSimpleTypeUnmarshall**](/windows/win32/Rpcndr/nf-rpcndr-ndrsimpletypeunmarshall?branch=master)
-   [**NdrStubCall2**](/windows/win32/Rpcndr/nf-rpcndr-ndrstubcall2?branch=master)
-   [**NdrStubForwardingFunction**](/windows/win32/Rpcproxy/nf-rpcproxy-ndrstubforwardingfunction?branch=master)
-   [**NdrStubGetBuffer**](/windows/win32/Rpcproxy/nf-rpcproxy-ndrstubgetbuffer?branch=master)
-   [**NdrStubInitialize**](/windows/win32/Rpcproxy/nf-rpcproxy-ndrstubinitialize?branch=master)
-   [**NdrUserMarshalBufferSize**](/windows/win32/Rpcndr/nf-rpcndr-ndrusermarshalbuffersize?branch=master)
-   [**NdrUserMarshalFree**](/windows/win32/Rpcndr/nf-rpcndr-ndrusermarshalfree?branch=master)
-   [**NdrUserMarshalMarshall**](/windows/win32/Rpcndr/nf-rpcndr-ndrusermarshalmarshall?branch=master)
-   [**MIDL\_STUB\_DESC**](/windows/win32/Rpcndr/ns-rpcndr-_midl_stub_desc?branch=master)
-   [**MIDL\_STUB\_MESSAGE**](/windows/win32/Rpcndr/ns-rpcndr-_midl_stub_message?branch=master)
-   [**ProxyFileInfo**](/windows/win32/Rpcproxy/ns-rpcproxy-tagproxyfileinfo?branch=master)
-   [**RPC\_MESSAGE**](/windows/win32/RpcdceP/ns-rpcdcep-_rpc_message?branch=master)

 

 





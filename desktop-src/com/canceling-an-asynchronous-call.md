---
title: Canceling an Asynchronous Call
description: A client can cancel an asynchronous call that is in progress if the call object implements the ICancelMethodCalls interface.
ms.assetid: 30a162f2-ce16-4ee6-8002-59216ac0e59a
ms.topic: article
ms.date: 05/31/2018
---

# Canceling an Asynchronous Call

A client can cancel an asynchronous call that is in progress if the call object implements the [**ICancelMethodCalls**](/windows/win32/api/objidlbase/nn-objidlbase-icancelmethodcalls) interface. For objects that use standard marshaling, **ICancelMethodCalls** is always available for marshaled calls. For objects that use custom marshaling or for calls to server objects within the same apartment, this functionality is available only if the call object implements **ICancelMethodCalls**.

The client can cancel the call at any time, from when the Begin\_ method is called until the Finish\_ method returns. If the client cancels the call before calling the Finish\_ method, it must call the Finish\_ method to clean up the state of the call object. Until the client has done so, any calls to any Begin\_ method on the call object will return RPC\_E\_CALL\_PENDING.

**To cancel an asynchronous call**

1.  Query the call object for [**ICancelMethodCalls**](/windows/win32/api/objidlbase/nn-objidlbase-icancelmethodcalls).

2.  Call [**ICancelMethodCalls::Cancel**](/windows/win32/api/objidlbase/nf-objidlbase-icancelmethodcalls-cancel), and then call [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) to release the pointer obtained by the [**QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q)) call in step 1.

3.  If the client has not called the Finish\_ method already, call it now.

There is no guarantee that the server actually stopped execution of the call. If the client's further work depends on some server state that the call may or may not have changed, the client should determine that state before proceeding.

## Related topics

<dl> <dt>

[Making an Asynchronous Call](making-an-asynchronous-call.md)
</dt> </dl>

 

 
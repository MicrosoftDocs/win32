---
title: Threading Differences between Direct3D Versions
description: Many multi-threaded programming models make use of synchronization primitives (such as mutexes) to create critical sections and prevent code from being accessed by more than one thread at a time.
ms.assetid: 0c4f984e-4dd0-4714-b911-592ca86d5dc0
ms.topic: article
ms.date: 05/31/2018
---

# Threading Differences between Direct3D Versions

Many multi-threaded programming models make use of synchronization primitives (such as mutexes) to create critical sections and prevent code from being accessed by more than one thread at a time.

However, the resource creation methods of the [**ID3D11Device**](/windows/desktop/api/D3D11/nn-d3d11-id3d11device) interface were designed to be re-entrant, without requiring synchronization primitives and critical sections. As a result, the resource creation methods are efficient and easy to use.



|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Differences between Direct3D 11, 10 and 9:<br/> Direct3D 11 defaults to mostly thread-safe and continues to allow applications to opt-out using D3D11\_CREATE\_DEVICE\_SINGLETHREADED. If applications opt-out of being thread-safe, they must adhere to threading rules. The runtime synchronizes threads on behalf of the application allowing concurrent threads to run. In fact, the synchronization in Direct3D 11 is more efficient than using the thread-safe layer in Direct3D 10.<br/> Direct3D 10 can support the execution of only one thread at a time. Direct3D 10 is fully thread safe and allows an application to opt-out of that behavior by using D3D10\_CREATE\_DEVICE\_SINGLE\_THREADED. <br/> Direct3D 9 does not default to thread safe. However, when you call [**CreateDevice**](/windows/desktop/api/d3d9/nf-d3d9-idirect3d9-createdevice) or [**CreateDeviceEx**](/windows/desktop/api/d3d9/nf-d3d9-idirect3d9ex-createdeviceex) to create a device, you can specify the D3DCREATE\_MULTITHREADED flag to make the Direct3D 9 API thread safe. This causes significant synchronization overhead. Therefore, making the Direct3D 9 API thread safe is not recommended because performance can be degraded.<br/> |



 

## Related topics

<dl> <dt>

[MultiThreading](overviews-direct3d-11-render-multi-thread.md)
</dt> </dl>

 


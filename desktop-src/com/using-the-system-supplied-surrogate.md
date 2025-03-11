---
title: Using the system-supplied surrogate
description: Using the system-supplied surrogate
ms.assetid: 6709e5e2-50e0-470f-b618-3d3043f6e180
ms.topic: concept-article
ms.date: 05/30/2024
---

# Using the system-supplied surrogate

To use the system-supplied surrogate for your DLL server, register the DLL specifying an empty string or **NULL** for the [DllSurrogate](dllsurrogate.md) value in the registry. When an activation request for a DLL server so designated comes to COM, COM launches the default surrogate process and the requested DLL (by specifying the CLSID on the launch command line internally) at the same time to avoid a separate call. (For information on running more than one DLL server in a surrogate process, see [Surrogate Sharing](surrogate-sharing.md).)

The default implementation of the surrogate process is a mixed-threading model style pseudo-COM server. When multiple DLL servers are loaded into a single surrogate process, this process ensures that each DLL server is instantiated using the threading model specified in the registry for that server. All loaded free-threaded servers will live together in the multithreaded apartment, while each apartment-threaded server will reside in a single-threaded apartment. If a DLL server supports both threading models, COM will choose multithreading.

This surrogate process is written so that COM handles both the unloading of DLL servers and the terminating of the surrogate process. The process lifetime is primarily informed by the number of marshaled objects in the surrogate, which acts as a heuristic measure of external dependencies on the process.Even though the intent is to represent external dependencies, this lifetime model doesn't distinguish between in-proc and out-of-proc marshaling. Take care to avoid unintentionally pinning the surrogate through cross-apartment marshaling, or through in-proc marshaling-based mechanisms such as the [Global Interface Table](creating-the-global-interface-table.md) or [IAgileReference](/windows/win32/api/objidl/nn-objidl-iagilereference).

The system-provided surrogate will work very well for most developers, as well as being very easy to use. However, those developers with special considerations may decide that a custom surrogate is necessary. For more information, see [Writing a Custom Surrogate](writing-a-custom-surrogate.md).

## Related topics

* [DLL surrogates](dll-surrogates.md)

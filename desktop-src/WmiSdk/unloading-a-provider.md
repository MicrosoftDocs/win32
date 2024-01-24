---
description: After WMI is finished with a provider, it unloads the provider from memory.
ms.assetid: 6116769f-3402-42b3-835d-9bdb0fc27ce0
ms.tgt_platform: multiple
title: Unloading a Provider
ms.topic: article
ms.date: 05/31/2018
---

# Unloading a Provider

After WMI is finished with a provider, it unloads the provider from memory. The primary reason WMI unloads a provider is to conserve system resources. Therefore, you must add code that allows WMI to unload your provider in an efficient manner. It takes anywhere from the interval specified in the cache control to twice that interval for WMI to unload a provider.

WMI unloads a provider in one of the following ways:

-   Unload a provider after the provider finishes the tasks given to it.
-   Quickly unload all providers when the user shuts down the system. Note that WMI unloads in-process providers when the WMI service is shut down from the command line.

While the first scenario is more common, you must write your provider for both possibilities.

The following sections are discussed in this topic:

-   [Unloading an Idle Provider](#unloading-an-idle-provider)
-   [Accessing the Idle Time for a Provider](#accessing-the-idle-time-for-a-provider)
-   [Unloading a Provider That Is Also a WMI Client](#unloading-a-provider-that-is-also-a-wmi-client)
-   [Unloading a Provider During Shutdown](#unloading-a-provider-during-shutdown)
-   [Related topics](#related-topics)

## Unloading an Idle Provider

WMI performs the following actions when it unloads an idle provider:

-   Determines if the provider is idle.

    WMI uses the **ClearAfter** property to determine how long a provider may stay idle before unloading that provider. For more information, see [Accessing the Idle Time for a Provider](#accessing-the-idle-time-for-a-provider).

-   Calls the [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) method of the provider.

    If the provider was a pure provider, then [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) completely removes the provider from active memory. However, a nonpure provider may continue to run after WMI calls **Release**.

## Accessing the Idle Time for a Provider

The minimum amount of time a provider remains active is determined by the **ClearAfter** property. You can find **ClearAfter** in instances of classes derived from the WMI system class [**\_\_CacheControl**](--cachecontrol.md) in the \\root namespace.

The following list describes the classes that are derived from [**\_\_CacheControl**](--cachecontrol.md), which controls provider unloading:

-   [**\_\_EventConsumerProviderCacheControl**](--eventconsumerprovidercachecontrol.md)
-   [**\_\_EventProviderCacheControl**](--eventprovidercachecontrol.md)
-   [**\_\_EventSinkCacheControl**](--eventsinkcachecontrol.md)
-   [**\_\_ObjectProviderCacheControl**](--objectprovidercachecontrol.md)
-   [**\_\_PropertyProviderCacheControl**](--propertyprovidercachecontrol.md)

You can change the minimum amount of time that WMI allows a provider to remain inactive by editing the **ClearAfter** property in the cache control instance for a specific type of provider. For example, to limit the amount of time a property provider can remain idle, you would edit the **ClearAfter** property of a [**\_\_PropertyProviderCacheControl**](--propertyprovidercachecontrol.md) instance in the \\root namespace.

## Unloading a Provider That Is Also a WMI Client

Your provider may need to remain a client of WMI after it has completed the provider functions it was called to perform. For example, a push provider may need to issue queries to WMI. For more information, see [Determining Push or Pull Status](determining-push-or-pull-status.md). In this case, the **Pure** property of the [**\_\_Win32Provider**](--win32provider.md) instance that represents the provider should be set to **TRUE**. If the **Pure** property is set to **FALSE**, the provider prepares to unload by calling [**IUnknown::Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) on all outstanding interface points when WMI calls the Release method of its primary interface. For more information, see the Remarks section in [**\_\_Win32Provider**](--win32provider.md).

The following procedure describes how to implement a release method for the primary interface of your provider.

**To unload a provider**

1.  Release all interface pointers held against WMI when WMI calls the [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) method of the primary interface of your provider.

    Typically, a provider holds pointers to the [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) and [**IWbemContext**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemcontext) interfaces supplied in [**IWbemProviderInit::Initialize**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemproviderinit-initialize).

2.  If the **Pure** property in the associated [**\_\_Win32Provider**](--win32provider.md) instance is set to **FALSE**, the provider can transition to the role of client application after WMI calls [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release). However, WMI cannot unload a provider that is operating as a client system, which increases the system overhead.

    A provider with **Pure** set to **TRUE** exists only to service requests. Therefore, this type of provider cannot take on the role of a client application and WMI can unload it.

## Unloading a Provider During Shutdown

Under normal circumstances, using the guidelines in [Unloading a Provider That is Also a WMI Client](#unloading-a-provider-that-is-also-a-wmi-client) allows WMI to unload your provider properly. However, you may run into situations where WMI is unable to instigate the normal unloading procedures, such as when the user chooses to shut the system down. By using a transaction model of data storage, in addition to implementing a good cleanup strategy, you can ensure that your provider is properly unloaded.

The user may stop WMI at any time. In such a situation, WMI does not unload any providers or call the [**DllCanUnloadNow**](/windows/win32/api/combaseapi/nf-combaseapi-dllcanunloadnow) entry point on any in-process provider. Moreover, if an in-process provider is in the middle of a method call at the time of the shutdown, WMI can possibly terminate the executing thread in the middle of the call. In this circumstance, WMI does not call routines that normally handle cleanup, such as an object destructor. At most, WMI will call [**DllMain**](/windows/desktop/Dlls/dllmain) only.

When the operating system shuts down WMI, the system automatically releases all memory allocated to an in-process provider. The operating system also closes most resources held by the provider, such as file handles, window handles, and so on. The provider does not need to take any specific action to make this happen.

Because WMI may shut down in the middle of a call, a provider should not leave data sources in an inconsistent state. Leaving your data in an inconsistent state is not a problem for read-only providers. However, providers with write capabilities may want to implement some sort of transaction model to allow a safe rollback after an abrupt termination.

While the operating system may release some general system resources, the system does not automatically release all resources. For example, the operating system may not release a socket or a database connection. Instead, the provider may need to manually clean up such resources. To avoid these problems, you can either implement your provider out-of-process, or you can add cleanup code.

The simplest solution is to implement your provider out-of-process. An out-of-process provider is not killed when WMI shuts down, although WMI will release the provider after a COM timeout. Providers for whom cleanup and termination robustness issues are more important than performance may be out-of-process.

If you must place cleanup code in your provider, you have two options. One place to perform this sort of cleanup is [**DllMain**](/windows/desktop/Dlls/dllmain), the DLL entry point function the operating system calls when unloading the DLL. Cleanup code can be added directly into **DllMain**, executing it in response to **DLL\_PROCESS\_DETACH**. Implementing cleanup code in **DllMain** can be somewhat difficult to arrange, especially in programming environments such as MFC or ATL. For more information, see the Microsoft Knowledge Base article Q148791, "*How to Provide Your Own DllMain in an MFC Regular DLL.*" (This resource may not be available in some languages and countries or regions.)

Alternately, you could also place the cleanup code in the destructor of a global class. For more information, see Unloading a Provider. The Windows operating system does not allocate global objects on the heap. Instead, the operating system calls the destructors during DLL unload.

The following is a simple cleanup procedure that could fit inside a global object for WMI.


```C++
class CMyCleanup
{
    ~CMyCleanup()
    {
        CloseHandle(m_hOpenFile);
        CloseDatabaseConnection(g_hDatabase);
    }
} g_Cleanup;
```



There are many restrictions as to what can be done in the cleanup code with either approach. For example, neither threads nor any DLLs that are not implicitly linked may be accessed in any way. Further, you cannot make COM calls under any circumstances.

## Related topics

<dl> <dt>

[Setting Namepace Security Descriptors](setting-namespace-security-descriptors.md)
</dt> <dt>

[Securing Your Provider](securing-your-provider.md)
</dt> <dt>

[Developing a WMI Provider](developing-a-wmi-provider.md)
</dt> </dl>

 

 

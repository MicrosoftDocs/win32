---
title: Virtualization Instance Lifecycle
description: Overview of the lifecycle of a ProjFS virtualization instance.
ms.assetid: <GUID-GOES-HERE>
ms.date: 09/17/2018
ms.topic: article
---

# Virtualization Instance Lifecycle

The provider application maintains one or more virtualization instances.  Each virtualization instance goes through four stages in its lifecycle:

1. Creation
2. Startup
3. Runtime
4. Shutdown

Note that after shutting down a virtualization instance the provider does not need to re-create it to reuse it.  It can simply start it up again.

> **Note**: This section shows examples of ProjFS APIs.  Each example is meant to illustrate basic API usage.  For documentation of options unused in these examples please consult the [ProjFS API reference](/windows/desktop/api/_projfs).

## Creating a virtualization root

Before a provider can start up the virtualization instance that will project items into the local file system, it must create the virtualization root.  The virtualization root is the directory under which the provider projects a tree of directories and files.

To create a virtualization root the provider must:

1. Create a directory to serve as the virtualization root.

    The provider creates a directory to serve as the virtualization root using, for example **[CreateDirectory](/windows/desktop/api/fileapi/nf-fileapi-createdirectoryw)**:

    ```C++
    HRESULT hr;
    const wchar_t* rootName = LR"(C:\virtRoot)";
    if (!CreateDirectoryW(rootName, nullptr))
    {
        hr = HRESULT_FROM_WIN32(GetLastError());
        wprintf(L"Failed to create virtualization root (0x%08x)\n", hr);
        return;
    }
    ```

1. Create a virtualization instance ID.

    Every virtualization instance has a unique ID called the _virtualization instance ID_.  The system uses this value to identify which virtualization instance its contents are associated to.

    ```C++
    GUID instanceId;
    hr = CoCreateGuid(&instanceId);
    if (FAILED(hr))
    {
        wprintf(L"Failed to create instance ID (0x%08x)\n", hr);
        return;
    }
    ```

1. Mark the new directory as the virtualization root.

    The provider calls **[PrjMarkDirectoryAsPlaceholder](/windows/desktop/api/projectedfslib/nf-projectedfslib-prjmarkdirectoryasplaceholder)** to mark the new directory as the virtualization root and assign it to the virtualization instance.

    ```C++
    hr = PrjMarkDirectoryAsPlaceholder(rootName,
                                       nullptr,
                                       nullptr,
                                       &instanceId);
    if (FAILED(hr))
    {
        wprintf(L"Failed to mark virtualization root (0x%08x)\n", hr);
        return;
    }
    ```

The provider only needs to create the virtualization root once for each virtualization instance.  Once a root has been created, its associated instance can be repeatedly started and stopped without recreating the root.

## Starting a virtualization instance

Once the virtualization root has been created the provider must start the virtualization instance.  This signals ProjFS that the provider is ready to receive callbacks and provide data.

To start the virtualization instance the provider must:

1. Set up the callback table.

    ProjFS communicates with the provider by invoking callback routines implemented by the provider.  The provider populates a [PRJ_CALLBACKS](/windows/desktop/api/projectedfslib/ns-projectedfslib-prj_callbacks) struct with pointers to its callback routines.

    ```C++
    PRJ_CALLBACKS callbackTable;

    // Supply required callbacks.
    callbackTable.StartDirectoryEnumerationCallback = MyStartEnumCallback;
    callbackTable.EndDirectoryEnumerationCallback = MyEndEnumCallback;
    callbackTable.GetDirectoryEnumerationCallback = MyGetEnumCallback;
    callbackTable.GetPlaceholderInfoCallback = MyGetPlaceholderInfoCallback;
    callbackTable.GetFileDataCallback = MyGetFileDataCallback;

    // The rest of the callbacks are optional.
    callbackTable.QueryFileNameCallback = nullptr;
    callbackTable.NotificationCallback = nullptr;
    callbackTable.CancelCommandCallback = nullptr;
    ```

1. Start the instance.

    The provider calls **[PrjStartVirtualizing](/windows/desktop/api/projectedfslib/nf-projectedfslib-prjstartvirtualizing)** to start the virtualization instance.

    ```C++
    PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT instanceHandle;
    hr = PrjStartVirtualizing(rootName,
                              &callbackTable,
                              nullptr,
                              nullptr,
                              &instanceHandle);
    if (FAILED(hr))
    {
        wprintf(L"Failed to start the virtualization instance (0x%08x)\n", hr);
        return;
    }
    ```
    **PrjStartVirtualizing**'s _instanceHandle_ parameter returns a handle to the virtualization instance.  The provider uses this handle when calling other ProjFS APIs.

## Virtualization instance runtime

Once the call to **PrjStartVirtualizing** returns, ProjFS will invoke the provider's callback routines in response to file system operations in the virtualization instance.  For information on how the provider can handle various file system operations, refer to the following sections:

* [Enumerating Files and Directories](enumerating-files-and-directories.md)
* [Providing File Data](providing-file-data.md)
* [File System Operation Notifications](file-system-operation-notifications.md)
* [Handling View Changes](handling-view-changes.md)

## Shutting down a virtualization instance

To signal ProjFS that the provider wants to stop receiving callbacks and providing data, the provider must stop the virtualization instance.  To do this the provider calls **[PrjStopVirtualizing](/windows/desktop/api/projectedfslib/nf-projectedfslib-prjstopvirtualizing)**, passing it the handle to the virtualization instance that it received from the call to **PrjStartVirtualizing**.

```C++
PrjStopVirtualizing(instanceHandle);
```

Note that until this call returns, ProjFS may continue to invoke the provider's callback routines.
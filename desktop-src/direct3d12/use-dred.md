---
title: Use DRED to diagnose GPU faults
description: Device Removed Extended Data (DRED) is an evolving set of diagnostic features designed to help you to identify the cause of unexpected device removal errors.
ms.custom: 19H1
ms.topic: article
ms.date: 04/19/2019
---

# Use DRED to diagnose GPU faults
DRED stands for Device Removed Extended Data. DRED is an evolving set of diagnostic features designed to help you to identify the cause of unexpected device removal errors. On hardware that supports the necessary features (as defined below), DRED delivers automatic breadcrumbs as well as GPU page fault reporting.

## Auto-breadcrumbs
To set the scene for auto-breadcrumbs, let's first mention the manual variety. In anticipation of the eventuality of a [Timeout Detection and Recovery (TDR)](/windows-hardware/drivers/display/timeout-detection-and-recovery), you can use the [ID3D12GraphicsCommandList2::WriteBufferImmediate method](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist2-writebufferimmediate) to place *breadcrumbs* into the GPU command stream, in order to track GPU progress.

This is a reasonable approach if you want to create a custom, low-overhead implementation. But it may lack some of the versatility of a standardized solution, such as debugger extensions, or reporting via [Windows Error Reporting (WER)](/windows/desktop/wer/windows-error-reporting) (also known as Watson).

So, DRED's auto-breadcrumbs call **WriteBufferImmediate** to place progress counters into the GPU command stream. DRED inserts a breadcrumb after each *render op*&mdash;which means every operation that results in GPU work (for example, **Draw**, **Dispatch**, **Copy**, **Resolve**, and others). If the device is removed in the middle of a GPU workload, then the DRED breadcrumb value is essentially a collection of the render ops that completed before the error.

The breadcrumb history ring buffer retains up to 64KiB operations in a given command list. If there are more than 65536 operations in a command list, then only the last 64KiB operations are stored&mdash;overwriting the oldest operations first. However, the breadcrumb counter value continues to count up to `UINT_MAX`. Therefore, LastOpIndex = (BreadcrumbCount - 1) % 65536.

DRED 1.0 was first available in Windows 10, version 1809 (Windows 10 October 2018 Update), and it exposed rudimentary auto-breadcrumbs. However, there were no APIs for it, and the only way to enable DRED 1.0 was to use **Feedback Hub** to capture a TDR reproduction (repro) for **Apps & Games** \> **Game Performance and Compatibility**. The primary purpose for DRED 1.0 was to help to root-cause-analyze game crashes via customer feedback.
### Caveats
- Because a GPU is heavily pipelined, there's no guarantee that the breadcrumb counter indicates the exact operation that failed. In fact, on some tile-based deferred render devices, it's possible for the breadcrumb counter to be a full resource or unordered access view (UAV) barrier behind the actual GPU progress.
- A display driver can reorder commands, pre-fetch from resource memory well before executing a command, or flush cached memory well-after completion of a command. Any of these can produce a GPU error. In such cases, the auto-breadcrumb counters may be less helpful, or misleading.
### Performance
Although auto-breadcrumbs are designed to be low-overhead, they are not free. Empirical measurements show 2-5% performance loss on a typical AAA Direct3D 12 graphics game engine. For this reason, auto-breadcrumbs are off by default.
### Hardware requirements
Because the breadcrumb counter values must be preserved after device removal, the resource that contains breadcrumbs must exist in system memory, and it must persist in the event of device removal. This means that the display driver needs to support [**D3D12_FEATURE_EXISTING_HEAPS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_feature). Fortunately, this is the case for most Direct3D 12 display drivers on Windows 10, version 1903.
## GPU page fault reporting
A feature that's new for DRED 1.1 is DRED GPU page fault reporting. A GPU page fault commonly occurs under one of these conditions.

1. An application mistakenly executes work on the GPU that references a deleted object. This is one of the top reasons for an unexpected device removal.
2. An application mistakenly executes work on the GPU that accesses an evicted resource, or a non-resident tile.
3. A shader references an uninitialized or stale descriptor.
3. A shader indexes beyond the end of a root binding.

DRED attempts to address some of these scenarios by reporting the names and types of any existing or recently freed API objects that match the virtual address (VA) of the GPU-reported page fault.

### Caveat
Not all GPUs support page faults (although, many do). Some GPUs respond to memory faults by: bit-bucket writes; reading simulated data (for example, zeros); or by simply hanging. Unfortunately, in cases where the GPU doesn't immediately hang, a [Timeout Detection and Recovery (TDR)](/windows-hardware/drivers/display/timeout-detection-and-recovery) can happen later in the pipe, making it even harder to locate the root cause.

### Performance
The Direct3D 12 runtime must actively curate a collection of existing and recently-deleted API objects indexable by virtual address (VA). This increases the system memory overhead, and introduces a small performance hit to object creation and destruction. For that reason, this behavior is off by default.

### Hardware requirements
A GPU that doesn't support page faulting can still benefit from the auto-breadcrumbs feature.

## Setting up DRED in code
DRED settings are global to the process, and you must configure them prior to creating a Direct3D 12 Device. To do so, call the [**D3D12GetDebugInterface**](/windows/desktop/api/d3d12/nf-d3d12-d3d12getdebuginterface) function to retrieve an [**ID3D12DeviceRemovedExtendedDataSettings**](/windows/desktop/api/d3d12/nn-d3d12-id3d12deviceremovedextendeddatasettings).

```cpp
CComPtr<ID3D12DeviceRemovedExtendedDataSettings> pDredSettings;
VERIFY_SUCCEEDED(D3D12GetDebugInterface(IID_PPV_ARGS(&pDredSettings)));

// Turn on auto-breadcrumbs and page fault reporting.
pDredSettings->SetAutoBreadcrumbsEnablement(D3D12_DRED_ENABLEMENT_FORCED_ON);
pDredSettings->SetPageFaultEnablement(D3D12_DRED_ENABLEMENT_FORCED_ON);
```

> [!NOTE]
> Modifications to DRED settings have no effect on devices already created. But subsequent calls to [**D3D12CreateDevice**](/windows/desktop/api/d3d12/nf-d3d12-d3d12createdevice) use the most recent DRED settings.

## Accessing DRED data in code
After device removal has been detected (for example, **Present** returns [**DXGI_ERROR_DEVICE_REMOVED**](/windows/desktop/com/com-error-codes-10)), use the methods of the [**ID3D12DeviceRemovedExtendedData**](/windows/desktop/api/d3d12/nn-d3d12-id3d12deviceremovedextendeddata) interface to access the DRED data for the removed device.

To retrieve the **ID3D12DeviceRemovedExtendedData** interface, call [QueryInterface](/windows/desktop/api/unknwn/nf-unknwn-iunknown-queryinterface(refiid_void)) on an [ID3D12Device](/windows/win32/api/d3d12/nn-d3d12-id3d12device) (or derived) interface, passing the interface identifier (IID) of **ID3D12DeviceRemovedExtendedData**.

```cpp
void MyDeviceRemovedHandler(ID3D12Device * pDevice)
{
    CComPtr<ID3D12DeviceRemovedExtendedData> pDred;
    VERIFY_SUCCEEDED(pDevice->QueryInterface(IID_PPV_ARGS(&pDred)));
    D3D12_DRED_AUTO_BREADCRUMBS_OUTPUT DredAutoBreadcrumbsOutput;
    D3D12_DRED_PAGE_FAULT_OUTPUT DredPageFaultOutput;
    VERIFY_SUCCEEDED(pDred->GetAutoBreadcrumbsOutput(&DredAutoBreadcrumbsOutput));
    VERIFY_SUCCEEDED(pDred->GetPageFaultAllocationOutput(&DredPageFaultOutput));
    // Custom processing of DRED data can be done here.
    // Produce telemetry...
    // Log information to console...
    // break into a debugger...
}
```

## Debugger access to DRED
Debuggers have access to the DRED data via the **d3d12!D3D12DeviceRemovedExtendedData** data export.

## DRED telemetry
Your application can use the DRED APIs to control DRED features, and to collect telemetry to help analyze problems. This gives you a much broader net for catching those hard-to-reproduce TDRs.

As of Windows 10, version 1903, all user-mode device-removed events are reported to [Windows Error Reporting (WER)](/windows/desktop/wer/windows-error-reporting), also known as Watson. If a particular combination of application, GPU, and display driver generates a sufficient number of device-removed events, then it's possible that DRED will be temporarily enabled for customers launching the same application on a similar configuration.

---
title: Get started with the WinI3C API
description: Walkthrough of enumerating a WinI3C-Target, initializing a library-managed handle, transferring data with I3C Private Reads and Writes, and receiving In-Band-Interrupts (IBIs) using the WinI3C user-mode API.
ms.topic: how-to
ms.date: 11/11/2026
---

# Get started with the WinI3C API

The WinI3C API lets a user-mode client, such as an application or service, communicate with an I3C Target device (*WinI3C-Target*) through an MIPI I3C HCI-compliant I3C HostController-Device that uses the inbox I3C driver stack. Broadcast and bus-management CCCs, such as ENEC and DEFGRPA, aren't permitted.

This article walks through the typical client flow:

1. Discover WinI3C-Targets by registering a vendor device-interface-class for added callbacks.
1. Initialize a WinI3C-Target into a library-managed [WinI3CTarget](/windows/win32/api/wini3c/wini3ctarget-handle) handle.
1. Configure Max Write/Read lengths.
1. Exchange data with I3C Private Writes and Reads.
1. Optionally, enable In-Band-Interrupts (IBIs).
1. Release resources.

The code in this article uses the **Library-managed WinI3C APIs**, which are the recommended way to use WinI3C. A parallel set of *Non-library-managed WinI3C APIs* (the `*WithFileHandle` and `*FromOperation` functions) exists for advanced scenarios where the client wants to own the file handle and drive overlapped I/O directly. Those APIs are generally not recommended. For the full API surface, see the [WinI3C API reference](/windows/win32/api/wini3c/).

## Prerequisites

- **Windows 11 25H2 October update (build 26200)** or later, on a system with an MIPI I3C HCI-compliant I3C HostController-Device that uses the inbox I3C driver stack.
- A **WinI3C Vendor Extension INF** that registers a vendor-defined device-interface-class for the relevant WinI3C-Targets. The client discovers WinI3C-Targets by this device-interface-class GUID. For background, see [Using an extension INF file](/windows-hardware/drivers/install/using-an-extension-inf-file).
- The `wini3c.h` header, first included in [Windows SDK 10.0.26100.9457](/windows/apps/windows-sdk/release-notes#build-100261009457). The SDK version identifies the header package, not the minimum Windows version required to run WinI3C.
- The [Windows Implementation Libraries (WIL)](https://github.com/microsoft/wil/wiki/Error-handling-helpers). The examples use `RETURN_IF_FAILED` and `LOG_IF_FAILED` from `<wil/result.h>`.

> [!IMPORTANT]
> The initial Windows releases that contain WinI3C don't include an import library (`wini3c.lib`). Apps targeting those releases must load functions dynamically from `wini3c.dll` by using [LoadLibrary](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibraryw) and [GetProcAddress](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress). Use the import library only on Windows releases that provide it.
>
> The examples below use the SDK function names to illustrate the call sequence and don't include dynamic-loading setup. Adapt the calls to use the resolved function pointers before building an application for releases without an import library.

> [!NOTE]
> Throughout this article, replace `GUID_DEVINTERFACE_MY_WINI3C_TARGET` with the device interface class GUID that your extension INF registers.

> [!NOTE]
> The snippets focus on the WinI3C calls. For brevity, they don't demonstrate comprehensive production error handling.

## Step 1: Enumerate WinI3C-Targets

WinI3C identifies WinI3C-Targets by the vendor device-interface-class GUID configured through a **WinI3C Vendor Extension INF**. Register this GUID with [WinI3CRegisterForTargetAdded](/windows/win32/api/wini3c/nf-wini3c-wini3cregisterfortargetadded) and provide a [WINI3CTARGETADDEDCALLBACK](/windows/win32/api/wini3c/nc-wini3c-wini3ctargetaddedcallback). The call **blocks until all existing matching WinI3C-Targets have been enumerated**, invoking your callback once per WinI3C-Target. New WinI3C-Targets that arrive later invoke the callback again.

```cpp
#include <windows.h>
#include <initguid.h>
#include <vector>
#include <string>

#include <wil/result.h>
#include <wini3c.h>

// TODO: Replace with valid GUID.
// {00000000-0000-0000-0000-000000000000}
DEFINE_GUID(GUID_DEVINTERFACE_MY_WINI3C_TARGET,
    0x00000000, 0x0000, 0x0000, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0, 0x00);

int main()
{
    std::vector<WinI3CTarget> initializedTargets;

    RETURN_IF_FAILED(WinI3CRegisterForTargetAdded(
        &GUID_DEVINTERFACE_MY_WINI3C_TARGET,
        &initializedTargets,
        [](
            _In_ void* pContext,
            _In_ const GUID* addedTargetDeviceInterfaceClass,
            _In_ const WCHAR* addedTargetDeviceInterfacePath)
        {
            // WINI3CTARGETADDEDCALLBACK, invoked when the WinI3C library detects a Target arriving.
        }));

    if (initializedTargets.empty())
    {
        return HRESULT_FROM_WIN32(ERROR_NOT_FOUND);
    }
}
```

## Step 2: Initialize a WinI3C-Target

For a discovered device-interface-path from [WINI3CTARGETADDEDCALLBACK](/windows/win32/api/wini3c/nc-wini3c-wini3ctargetaddedcallback), invoke [WinI3CInitializeTarget](/windows/win32/api/wini3c/nf-wini3c-wini3cinitializetarget). The library opens and manages the file handle for you and returns a [WinI3CTarget](/windows/win32/api/wini3c/wini3ctarget-handle) through the [WINI3CTARGETINITIALIZEDCALLBACK](/windows/win32/api/wini3c/nc-wini3c-wini3ctargetinitializedcallback). Supply a [WINI3CTARGETREMOVEDCALLBACK](/windows/win32/api/wini3c/nc-wini3c-wini3ctargetremovedcallback) so you can react when the WinI3C-Target is unplugged or removed. The removed handle must be destroyed with [WinI3CRelease](/windows/win32/api/wini3c/nf-wini3c-wini3crelease), never [CloseHandle](/windows/win32/api/handleapi/nf-handleapi-closehandle).

```cpp
int main()
{
    std::vector<WinI3CTarget> initializedTargets;

    RETURN_IF_FAILED(WinI3CRegisterForTargetAdded(
        &GUID_DEVINTERFACE_MY_WINI3C_TARGET,
        &initializedTargets,
        [](
            _In_ void* pContext,
            _In_ const GUID* addedTargetDeviceInterfaceClass,
            _In_ const WCHAR* addedTargetDeviceInterfacePath)
        {
            // WINI3CTARGETADDEDCALLBACK, invoked when the WinI3C library detects a Target arriving.

            LOG_IF_FAILED(WinI3CInitializeTarget(
                addedTargetDeviceInterfacePath,
                pContext,
                [](
                    _In_ void* pContext,
                    _In_ WinI3CTarget initializedTarget)
                {
                    // WINI3CTARGETINITIALIZEDCALLBACK, invoked when a WinI3CTarget is successfully initialized.

                    std::vector<WinI3CTarget>* pInitializedTargets = (std::vector<WinI3CTarget>*)pContext;

                    pInitializedTargets->push_back(initializedTarget);
                },
                pContext,
                [](
                    _In_ void* pContext,
                    _In_ WinI3CTarget removedTarget)
                {
                    // WINI3CTARGETREMOVEDCALLBACK, invoked when a WinI3C-Target has been removed.

                    // Handle removal.

                    WinI3CRelease(removedTarget);
                }));
        }));

    if (initializedTargets.empty())
    {
        return HRESULT_FROM_WIN32(ERROR_NOT_FOUND);
    }

    WinI3CTarget firstFoundTarget = initializedTargets[0];
}
```

## Step 3: Configure Max Write/Read lengths

Before I/O, advertise the maximum write and read sizes to the WinI3C-Target with [WinI3CSetMaxWriteLength](/windows/win32/api/wini3c/nf-wini3c-wini3csetmaxwritelength) and [WinI3CSetMaxReadAndIbiLength](/windows/win32/api/wini3c/nf-wini3c-wini3csetmaxreadandibilength).

[WinI3CSetMaxReadAndIbiLength](/windows/win32/api/wini3c/nf-wini3c-wini3csetmaxreadandibilength) is mandatory if you later enable IBIs with [WinI3CEnableIbis](/windows/win32/api/wini3c/nf-wini3c-wini3cenableibis) or [WinI3CEnableIbisWithAutoCommandRead](/windows/win32/api/wini3c/nf-wini3c-wini3cenableibiswithautocommandread).

```cpp
    const uint16_t requestedMaxWriteLength = ...;
    uint16_t actualMaxWriteLength;
    RETURN_IF_FAILED(WinI3CSetMaxWriteLength(firstFoundTarget, requestedMaxWriteLength, &actualMaxWriteLength));

    const uint16_t requestedMaxReadAndAutoCommandReadLength = ...;
    uint16_t actualMaxReadAndAutoCommandReadLength;
    const uint8_t requestedMaxIbiLength = ...;
    uint8_t actualMaxIbiLength;
    RETURN_IF_FAILED(WinI3CSetMaxReadAndIbiLength(
        firstFoundTarget,
        requestedMaxReadAndAutoCommandReadLength,
        &actualMaxReadAndAutoCommandReadLength,
        requestedMaxIbiLength,
        &actualMaxIbiLength));
```

Use the actual lengths accepted by the WinI3C-Target when you size subsequent transfers and IBI handling.

## Step 4: Write and read data

Use [WinI3CWrite](/windows/win32/api/wini3c/nf-wini3c-wini3cwrite) and [WinI3CRead](/windows/win32/api/wini3c/nf-wini3c-wini3cread) for I3C Private Writes and Reads. Both can take a preferred [WINI3C_TARGET_MODE](/windows/win32/api/wini3c/ne-wini3c-wini3c_target_mode). For SDR, pass **NULL** for the HDR command-code parameter.

For a combined write-then-read, use [WinI3CWriteRead](/windows/win32/api/wini3c/nf-wini3c-wini3cwriteread). Other combinations or types of transfer sequence aren't supported. For more complex sequences, call [WinI3CRead](/windows/win32/api/wini3c/nf-wini3c-wini3cread), [WinI3CWrite](/windows/win32/api/wini3c/nf-wini3c-wini3cwrite), or [WinI3CWriteRead](/windows/win32/api/wini3c/nf-wini3c-wini3cwriteread) multiple times.

For Vendor Direct Common Command Codes (CCCs) (`0xE0`-`0xFE`), use [WinI3CWriteVendorCcc](/windows/win32/api/wini3c/nf-wini3c-wini3cwritevendorccc) and [WinI3CReadVendorCcc](/windows/win32/api/wini3c/nf-wini3c-wini3creadvendorccc).

```cpp
    std::vector<uint8_t> writePayload = { 0x01, 0x02, 0x03 };
    if (writePayload.size() > actualMaxWriteLength)
    {
        return HRESULT_FROM_WIN32(ERROR_INSUFFICIENT_BUFFER);
    }

    RETURN_IF_FAILED(WinI3CWrite(firstFoundTarget, WinI3CTargetModeSdr, 0, (uint32_t)writePayload.size(), writePayload.data()));

    const uint32_t requestedReadPayloadSize = ...;
    if (requestedReadPayloadSize > actualMaxReadAndAutoCommandReadLength)
    {
        return HRESULT_FROM_WIN32(ERROR_INSUFFICIENT_BUFFER);
    }

    uint8_t readPayload[requestedReadPayloadSize] = { 0 };
    uint32_t actualReadPayload1Size = 0;
    RETURN_IF_FAILED(WinI3CRead(firstFoundTarget, WinI3CTargetModeSdr, nullptr, requestedReadPayloadSize, readPayload, &actualReadPayload1Size));
```

## Step 5 (optional): Receive In-Band-Interrupts (IBIs)

I3C In-Band-Interrupts (IBIs) allow WinI3C-Targets to send unsolicited payload without an additional GPIO-line, as in I2C implementations. This is particularly useful for sensors.

Auto-Command-Read is a convenience to increase throughput by configuring the HostController-Instance to trigger a read based on the received IBI Mandatory-Data-Byte (MDB).

To receive IBIs from a WinI3C-Target:

1. The WinI3C-Target must support IBIs.
1. Advertise the maximum IBI payload with [WinI3CSetMaxReadAndIbiLength](/windows/win32/api/wini3c/nf-wini3c-wini3csetmaxreadandibilength).
1. Call [WinI3CEnableIbis](/windows/win32/api/wini3c/nf-wini3c-wini3cenableibis) with a [WINI3CIBIRECEIVEDCALLBACK](/windows/win32/api/wini3c/nc-wini3c-wini3cibireceivedcallback). To configure an IBI Auto-Command-Read alongside each IBI, use [WinI3CEnableIbisWithAutoCommandRead](/windows/win32/api/wini3c/nf-wini3c-wini3cenableibiswithautocommandread) instead.
1. Call [WinI3CDisableIbis](/windows/win32/api/wini3c/nf-wini3c-wini3cdisableibis) when done.

```cpp
    RETURN_IF_FAILED(WinI3CEnableIbis(
        firstFoundTarget,
        nullptr,
        [](
            _In_opt_ void* ibiReceivedCallbackContext,
            _In_ WinI3CTarget target,
            _When_(ibiPayload == NULL, _In_range_(0, 0)) UINT32 ibiPayloadSize,
            _In_reads_bytes_opt_(ibiPayloadSize) const void* ibiPayload)
        {
            // WINI3CIBIRECEIVEDCALLBACK, invoked when an IBI has been received for a specific WinI3CTarget.
        }));

    ...

    RETURN_IF_FAILED(WinI3CDisableIbis(firstFoundTarget));
```

## Step 6: Release resources

Once communication with the WinI3C-Target is finished, destroy each [WinI3CTarget](/windows/win32/api/wini3c/wini3ctarget-handle) with [WinI3CRelease](/windows/win32/api/wini3c/nf-wini3c-wini3crelease) and unregister added-callback notifications with [WinI3CUnregisterForTargetAdded](/windows/win32/api/wini3c/nf-wini3c-wini3cunregisterfortargetadded).

The previously registered [WINI3CTARGETREMOVEDCALLBACK](/windows/win32/api/wini3c/nc-wini3c-wini3ctargetremovedcallback) won't be invoked if a [WinI3CTarget](/windows/win32/api/wini3c/wini3ctarget-handle) is destroyed with [WinI3CRelease](/windows/win32/api/wini3c/nf-wini3c-wini3crelease).

```cpp
    WinI3CRelease(firstFoundTarget);

    RETURN_IF_FAILED(WinI3CUnregisterForTargetAdded(&GUID_DEVINTERFACE_MY_WINI3C_TARGET));
```

## Putting it together

```cpp
#include <windows.h>
#include <initguid.h>
#include <vector>
#include <string>

#include <wil/result.h>
#include <wini3c.h>

// TODO: Replace with valid GUID.
// {00000000-0000-0000-0000-000000000000}
DEFINE_GUID(GUID_DEVINTERFACE_MY_WINI3C_TARGET,
    0x00000000, 0x0000, 0x0000, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0, 0x00);

int main()
{
    std::vector<WinI3CTarget> initializedTargets;

    // Step 1: Enumerate WinI3C-Targets.

    RETURN_IF_FAILED(WinI3CRegisterForTargetAdded(
        &GUID_DEVINTERFACE_MY_WINI3C_TARGET,
        &initializedTargets,
        [](
            _In_ void* pContext,
            _In_ const GUID* addedTargetDeviceInterfaceClass,
            _In_ const WCHAR* addedTargetDeviceInterfacePath)
        {
            // WINI3CTARGETADDEDCALLBACK, invoked when the WinI3C library detects a Target arriving.

            // Step 2: Initialize a WinI3C-Target.

            LOG_IF_FAILED(WinI3CInitializeTarget(
                addedTargetDeviceInterfacePath,
                pContext,
                [](
                    _In_ void* pContext,
                    _In_ WinI3CTarget initializedTarget)
                {
                    // WINI3CTARGETINITIALIZEDCALLBACK, invoked when a WinI3CTarget is successfully initialized.

                    std::vector<WinI3CTarget>* pInitializedTargets = (std::vector<WinI3CTarget>*)pContext;

                    pInitializedTargets->push_back(initializedTarget);
                },
                pContext,
                [](
                    _In_ void* pContext,
                    _In_ WinI3CTarget removedTarget)
                {
                    // WINI3CTARGETREMOVEDCALLBACK, invoked when a WinI3C-Target has been removed.

                    // Handle removal.

                    WinI3CRelease(removedTarget);
                }));
        }));

    if (initializedTargets.empty())
    {
        return HRESULT_FROM_WIN32(ERROR_NOT_FOUND);
    }

    WinI3CTarget firstFoundTarget = initializedTargets[0];

    // Step 3: Configure Max Write/Read lengths.

    const uint16_t requestedMaxWriteLength = 256; // Replace with a device-specific value.
    uint16_t actualMaxWriteLength;
    RETURN_IF_FAILED(WinI3CSetMaxWriteLength(firstFoundTarget, requestedMaxWriteLength, &actualMaxWriteLength));

    const uint16_t requestedMaxReadAndAutoCommandReadLength = 256; // Replace with a device-specific value.
    uint16_t actualMaxReadAndAutoCommandReadLength;
    const uint8_t requestedMaxIbiLength = 16; // Replace with a device-specific value.
    uint8_t actualMaxIbiLength;
    RETURN_IF_FAILED(WinI3CSetMaxReadAndIbiLength(
        firstFoundTarget,
        requestedMaxReadAndAutoCommandReadLength,
        &actualMaxReadAndAutoCommandReadLength,
        requestedMaxIbiLength,
        &actualMaxIbiLength));

    // Step 4: Write and read data.

    std::vector<uint8_t> writePayload = { 0x01, 0x02, 0x03 };
    if (writePayload.size() > actualMaxWriteLength)
    {
        return HRESULT_FROM_WIN32(ERROR_INSUFFICIENT_BUFFER);
    }

    RETURN_IF_FAILED(WinI3CWrite(firstFoundTarget, WinI3CTargetModeSdr, 0, (uint32_t)writePayload.size(), writePayload.data()));

    const uint32_t requestedReadPayloadSize = 256; // Replace with a device-specific value.
    if (requestedReadPayloadSize > actualMaxReadAndAutoCommandReadLength)
    {
        return HRESULT_FROM_WIN32(ERROR_INSUFFICIENT_BUFFER);
    }

    uint8_t readPayload[requestedReadPayloadSize] = { 0 };
    uint32_t actualReadPayload1Size = 0;
    RETURN_IF_FAILED(WinI3CRead(firstFoundTarget, WinI3CTargetModeSdr, nullptr, requestedReadPayloadSize, readPayload, &actualReadPayload1Size));

    // Step 5 (optional): Receive In-Band-Interrupts (IBIs).

    RETURN_IF_FAILED(WinI3CEnableIbis(
        firstFoundTarget,
        nullptr,
        [](
            _In_opt_ void* ibiReceivedCallbackContext,
            _In_ WinI3CTarget target,
            _When_(ibiPayload == NULL, _In_range_(0, 0)) UINT32 ibiPayloadSize,
            _In_reads_bytes_opt_(ibiPayloadSize) const void* ibiPayload)
        {
            // WINI3CIBIRECEIVEDCALLBACK, invoked when an IBI has been received for a specific WinI3CTarget.
        }));

    // Receive IBIs until the client no longer needs them.

    // Step 6: Release resources.

    RETURN_IF_FAILED(WinI3CDisableIbis(firstFoundTarget));

    WinI3CRelease(firstFoundTarget);

    RETURN_IF_FAILED(WinI3CUnregisterForTargetAdded(&GUID_DEVINTERFACE_MY_WINI3C_TARGET));
}
```

## Related topics

- [WinI3C API reference](/windows/win32/api/wini3c/)
- [WinI3CTarget handle](/windows/win32/api/wini3c/wini3ctarget-handle)
- [WinI3CAsyncOperation handle](/windows/win32/api/wini3c/wini3casyncoperation-handle)
- [WinI3CRegisterForTargetAdded](/windows/win32/api/wini3c/nf-wini3c-wini3cregisterfortargetadded)
- [WinI3CInitializeTarget](/windows/win32/api/wini3c/nf-wini3c-wini3cinitializetarget)
- [WinI3CWrite](/windows/win32/api/wini3c/nf-wini3c-wini3cwrite)
- [WinI3CRead](/windows/win32/api/wini3c/nf-wini3c-wini3cread)
- [WinI3CEnableIbis](/windows/win32/api/wini3c/nf-wini3c-wini3cenableibis)
- [WinI3CRelease](/windows/win32/api/wini3c/nf-wini3c-wini3crelease)
- [Devices](../devices.md)
- [Using an extension INF file](/windows-hardware/drivers/install/using-an-extension-inf-file)

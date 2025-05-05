---
description: Development guide for Virtualization-based security (VBS) enclaves - Learn how to build a basic VBS enclave.
title: VBS Enclaves Development Guide
titleSuffix: Secure Enclaves
ms.topic: how-to
ms.date: 11/20/2024
#customer intent: As a VBS Enclaves developer, I want to understand how to get started with enclaves so that I can develop my apps on the platform.
---

# Development guide for Virtualization-based security (VBS) Enclaves

[!INCLUDE [enclaves-os-reqs.md](../includes/enclaves-os-reqs.md)]

This development guide describes how to build, sign, and debug a basic VBS enclave.

## Prerequisites

To get started with VBS Enclaves, you need to meet the following requirements:

- View and satisfy device requirements in the [VBS Enclaves overview](/windows/win32/trusted-execution/vbs-enclaves#device-requirements).
- View and satisfy development prerequisites in the [VBS Enclaves overview](/windows/win32/trusted-execution/vbs-enclaves#development-prerequisites).
  - It's recommended to install the **Desktop development with C++** workload through the Visual Studio installer. It will install all the necessary tools including the Windows Software Development Kit (SDK).
- Download the [sample code](https://github.com/microsoft/Windows-classic-samples/tree/main/Samples/VbsEnclave) from GitHub. It demonstrates the life cycle of a VBS enclave including how to make function calls into the enclave.
  - Every enclave must have a host app. The sample code contains a Visual Studio Solution with two projects – the *enclave host* and the *test enclave*.

> [!WARNING]
> Ensure you have reviewed the OS support for VBS enclaves above, as support has recently changed.

## Getting started

After satisfying the prerequisites above, you should be able to open the solution file from the **VbsEnclave** sample in Visual Studio and compile it. It creates a test application along with the corresponding enclave. However, you can't run your application successfully until the enclave is signed with a valid certificate.

This guide details how to build a basic VBS enclave on your development machine. The steps to building a VBS enclave are:

1. Write a VBS enclave DLL and a corresponding host application
1. Compile the DLL and host
1. Sign the VBS enclave DLL
1. Debug the VBS enclave

Let’s start by understanding an enclave’s lifecycle. The enclave APIs are called in the following order:

:::image type="content" source="../images/vbs-enclaves-lifecycle-diagram.png" alt-text="Diagram illustrating the order in which VBS Enclaves APIs are called":::

## Step 1: Writing VBS enclaves

Let's examine the sample code and understand how to write an application that employs a VBS enclave.

### Writing the enclave Host

Remember that a VBS enclave DLL is simply a DLL, and so it requires a host application. The host application is nothing but a standard Windows application. To employ VBS enclaves, the host must use Windows enclave APIs from the [enclaveapi.h header](/windows/win32/api/enclaveapi/). Including `windows.h` in your host application will provide access to these APIs.

### Writing the DLL to load into a test enclave

*Refer to sample code in the **Test enclave** project to follow along with the steps below.*

In our enclave Sample, we create a simple enclave which XORs the input with `0xDADAF00D` and returns the result. Let’s break down how we do that:

1. Start by including `winenclave.h`. In the sample code, refer to `Samples/VbsEnclave/Test enclave/precomp.h`:

    ```c
    #include <winenclave.h>
    ```

    `winenclave.h` is the central include file for VBS enclaves and itself includes `windows.h`, `ntenclv.h`, `winenclaveapi.h`.

1. Every DLL loaded in an enclave requires a configuration. This configuration is defined using a global `const` variable named `__enclave_config` of type [IMAGE_ENCLAVE_CONFIG](/windows/win32/api/winnt/ns-winnt-image_enclave_config64). In the sample code, refer to `Samples/VbsEnclave/Test enclave/enclave.c`:

    ```c
    const IMAGE_ENCLAVE_CONFIG __enclave_config = {
        sizeof(IMAGE_ENCLAVE_CONFIG),
        IMAGE_ENCLAVE_MINIMUM_CONFIG_SIZE,
        IMAGE_ENCLAVE_POLICY_DEBUGGABLE,    // DO NOT SHIP DEBUGGABLE ENCLAVES TO PRODUCTION
        0,
        0,
        0,
        { 0xFE, 0xFE },    // family id
        { 0x01, 0x01 },    // image id
        0,                 // version
        0,                 // SVN
        0x10000000,        // size
        16,                // number of threads
        IMAGE_ENCLAVE_FLAG_PRIMARY_IMAGE
    };
    ```

    > [!NOTE]
    > There can be only one primary image per enclave. If you load multiple primary images, the one loaded first is treated as primary and the rest are treated as dependencies. In this sample, there are no dependencies other than the enclave platform DLLs.

1. The `DllMain()` function is mandatory and defines the entry point into the enclave. It's called during `InitializeEnclave()`. In the sample code, refer to `Samples/VbsEnclave/Test enclave/enclave.c`.

    ```c
    BOOL
    DllMain(
        _In_ HINSTANCE hinstDLL,
        _In_ DWORD dwReason,
        _In_ LPVOID lpvReserved
    )
    {
        UNREFERENCED_PARAMETER(hinstDLL);
        UNREFERENCED_PARAMETER(lpvReserved);
      
        if (dwReason == DLL_PROCESS_ATTACH) {
            InitialCookie = 0xDADAF00D;
        }
      
        return TRUE;
    }
    ```

1. Any functions inside the enclave that are called from the host application must be exported and be of type **LPENCLAVE_ROUTINE**. The function signature looks like this:

    ```c
    void* CALLBACK enclaveFunctionName(_In_ void* Context)
    ```

    In the sample code, refer to `Samples/VbsEnclave/Test enclave/enclave.c`.

    ```c
    void*
    CALLBACK
    CallEnclaveTest(
        _In_ void* Context
    )
    {
        WCHAR String[32];
        swprintf_s(String, ARRAYSIZE(String), L"%s\n", L"CallEnclaveTest started");
        OutputDebugStringW(String);
      
        return (void*)((ULONG_PTR)(Context) ^ InitialCookie);
    }
    ```

    > [!NOTE]
    > Only the functions exported by the primary enclave image can be accessed from the host application.

    You can then export the function using a `.DEF` file. In the sample code, refer to `Samples/VbsEnclave/Test enclave/vbsenclave.def`. For more information, refer to [Exporting from a DLL Using DEF Files](/cpp/build/exporting-from-a-dll-using-def-files).

And that’s how you write a basic VBS enclave DLL.

> [!IMPORTANT]
> Please note that to read/write Normal (non-enclave) memory, using the enclave memory accessors ([EnclaveCopyOutOfEnclave](/windows/win32/api/winenclaveapi/nf-winenclaveapi-enclavecopoutofenclave) and [EnclaveCopyIntoEnclave](/windows/win32/api/winenclaveapi/nf-winenclaveapi-enclavecopyintoenclave)) is strongly recommended. Please ensure all memory accesses to normal memory are made via these accessors.

## Step 2: Compiling VBS enclaves

Now that we’ve written our VBS enclave DLL, let’s compile it.

### Compiling the enclave host

Compiling the host app is the same as compiling any Windows application, but with the addition of `onecore.lib` to the list of dependencies while linking.

### Compiling the test enclave DLL

Before we can build the test enclave DLL, some changes to the compiler and linker configurations are required:

1. The MSVC linker provides an `/ENCLAVE` flag which picks up the enclave configuration details. The `/ENCLAVE` flag is incompatible with incremental linking, so we need to set `/INCREMENTAL:NO`.
1. *[Debug config only]* `/EDITANDCONTINUE` is incompatible with `/INCREMENTAL:NO`, so we use `/Zi` instead of `/ZI` for **Debug Information Format** in the compiler.
1. *[Debug config only]* The **Basic Runtime Checks** configuration needs to be set to **Default**. Runtime error checks are not supported in VBS enclaves.
1. An enclave DLL's digital signature must be checked at load time and requires setting the `/INTEGRITYCHECK` flag in the linker.
1. Enclave DLLs must be instrumented for **Control Flow Guard (CFG)**, for which we use the `/GUARD:MIXED` flag in the linker.
1. Enclaves have their own versions of platform, startup, runtime and UCRT libs. To ensure that we don't link the non-enclave versions, use the `/NODEFAULTLIB` flag. Subsequently, add the correct libs under `AdditionalDependencies`. In the sample code, these libraries are encapsulated under the **VBS_Enclave_Dependencies** macro. The following are the VBS enclave libraries:

    1. `libcmt.lib` and `libvcruntime.lib` - Found in the `enclave` folder with the Visual C++ build tools, see [C runtime (CRT) and C++ standard library (STL) .lib files](/cpp/c-runtime-library/crt-library-features).
    1. `vertdll.lib` and `bcrypt.lib` - Found in the `um` folder with the Windows SDK libraries.
    1. `ucrt.lib` - Found in the `ucrt_enclave` folder with the Windows SDK libraries.

> [!NOTE]
> No other platform libraries are supported within VBS enclaves.

In summary, the following changes are required:

*Compiler (Debug config only):*

- Debug Information Format: `/Zi`
- Basic Runtime Checks: `Default`

*Linker:*

- `/ENCLAVE`
- `/NODEFAULTLIBS` + `AdditionalDependencies`
- `/INCREMENTAL:NO`
- `/INTEGRITYCHECK`
- `/GUARD:MIXED`

You can now compile the enclave DLL.

### Securing with VEIID

**VEIID** (the VBS Enclave Import ID binding utility) is a tool in the Windows SDK that updates the import tables inside a VBS enclave with known IDs for platform DLLs. This improves the security of VBS enclaves by preventing a malicious (signed) DLL with the same name as one of the platform DLLs from being loaded.

In the sample code, this is done automatically as a post-build event.

> [!NOTE]
> It is strongly recommended to avoid using your own non-primary DLLs apart from the platform DLLs. Instead, keep all your code within the enclave DLL itself.

## Step 3: Signing VBS enclave DLLs

VBS enclaves must be signed to be successfully loaded. The signature on an enclave contains information about the enclave author. This is used to derive the Author ID for an enclave. You can test-sign your enclave before you sign it for production.

### Test Signing – Local

Each enclave signing certificate requires at least 3 EKUs:

1. Code Signing EKU - `1.3.6.1.5.5.7.3.3`
1. Enclave EKU - `1.3.6.1.4.1.311.76.57.1.15`
1. Author EKU - The EKU is of the form `1.3.6.1.4.1.311.97.X.Y.Z...`, where `X` is greater than `999`. The `...` indicates additional values in the EKU format. See the example below for clarification.

    For testing, you can choose to use any Author EKU that matches this pattern. For production, an Author EKU will be provided as part of the production certificate (more details on production signing are [below](#production-signing--trusted-signing-formerly-azure-code-signing)).

    Example: `1.3.6.1.4.1.311.97.814040577.346743379.4783502.105532346`

If you want to sign your enclave DLL while developing it, [enable test signing](/windows-hardware/drivers/install/the-testsigning-boot-configuration-option). With test signing enabled, you can create a certificate containing these three EKUs and sign your enclave with it. You can use the [New-SelfSignedCertificate](/powershell/module/pki/new-selfsignedcertificate?view=windowsserver2022-ps&preserve-view=true) cmdlet to create a certificate. **Note that Enclave DLLs must be page hash signed.**

> [!NOTE]
> Once you have a certificate, you can automate the signing process in the post-build event.

```powershell
New-SelfSignedCertificate -CertStoreLocation Cert:\\CurrentUser\\My -DnsName "MyTestEnclaveCert" -KeyUsage DigitalSignature -KeySpec Signature -KeyLength 2048 -KeyAlgorithm RSA -HashAlgorithm SHA256 -TextExtension "2.5.29.37={text}1.3.6.1.5.5.7.3.3,1.3.6.1.4.1.311.76.57.1.15,1.3.6.1.4.1.311.97.814040577.346743379.4783502.105532346"
```

```powershell
signtool sign /ph /fd SHA256 /n "MyTestEnclaveCert" vbsenclave.dll
```

With your enclave DLL signed, you can now load it in an environment that has test signing enabled.

### Production Signing – Trusted Signing (formerly Azure Code Signing)

Production signing for enclaves is provided through the **VBS enclave certificate profile** in [Trusted Signing](https://azure.microsoft.com/products/trusted-signing). For details on how to use **Trusted Signing**, please see the [documentation](/azure/trusted-signing/).

Trusted Signing also allows you to sign your enclave at the command line. This outputs a ready-to-run, signed enclave when you build your enclave in Visual Studio.

## Step 4: Debugging VBS enclaves

Typically, an enclave’s memory is hidden from debuggers and is protected from VTL0. However, if you wish to debug your VBS enclave DLL, you can build them to be debugged during development. Enclaves are a VTL1 user-mode process, and therefore can be debugged with a user-mode debugger.

To make your enclave debuggable:

1. **The enclave DLL image configuration needs to allow debugging** – This is done by setting the **IMAGE_ENCLAVE_POLICY_DEBUGGABLE** flag in [IMAGE_ENCLAVE_CONFIG](/windows/win32/api/winnt/ns-winnt-image_enclave_config64).
1. **Debugging needs to be allowed during enclave creation** – This is done by setting the **ENCLAVE_VBS_FLAG_DEBUG** flag in the [ENCLAVE_CREATE_VBS_INFO](/windows/win32/api/winnt/ns-winnt-enclave_create_info_vbs) structure passed to the [CreateEnclave](/windows/win32/api/enclaveapi/nf-enclaveapi-createenclave) call.

To debug your enclave:

1. Attach the user-mode debugger to the enclave host process.
1. Reload the enclave symbols after the host process has loaded the enclave image in memory.
1. Set breakpoints on the functions inside the enclave. The debugger breaks into it on an enclave call.

You can also break on the user-mode breakpoints for **CreateEnclave**, **InitializeEnclave**, etc. which further step into the corresponding code in `ntdll.dll`.

> [!NOTE]
> Never use debuggable enclaves in production environments.

With that, you can now build and deploy your first VBS enclave. If you have any questions, please reach out to [Windows developer support](https://developer.microsoft.com/windows/support/?tabs=Contact-us).

## Related content

[VBS Enclaves overview](vbs-enclaves.md)

[Azure Trusted Signing](/azure/trusted-signing/)

[enclaveapi.h header](/windows/win32/api/enclaveapi/)

[APIs available in VBS enclaves](available-in-enclaves.md)

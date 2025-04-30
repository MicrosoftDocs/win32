---
description: A Virtualization-based security (VBS) Enclave is a software-based trusted execution environment inside the address space of a host application.
ms.assetid: c6b272ee-c284-4c49-b12d-6a49b0315281
title: Virtualization-based security (VBS) enclaves
titleSuffix: Secure Enclaves
ms.topic: concept-article
ms.date: 11/20/2024
# customer intent: To learn about the Virtualization-based security (VBS) Enclaves feature in Windows.
---

# Virtualization-based security (VBS) enclaves

[!INCLUDE [enclaves-os-reqs.md](../includes/enclaves-os-reqs.md)]

A Virtualization-based security (VBS) Enclave is a software-based trusted execution environment inside the address space of a host application. VBS Enclaves leverage underlying [VBS technology](/windows-hardware/design/device-experiences/oem-vbs) to isolate the sensitive portion of an application in a secure partition of memory. VBS Enclaves enable isolation of sensitive workloads from both the host application and the rest of the system.

By planning ahead and isolating the sensitive part of your workload, you can isolate it in a VBS Enclave, as illustrated in the following diagram:

:::image type="content" source="../images/trusted-execution-enclaves-diagram.png" alt-text="Diagram of the VBS Enclaves trusted execution environment":::

## Device requirements

The following are required to run VBS Enclaves:

- VBS/HVCI must be enabled. This should be enabled on Windows 11 or later by default. See [Enable virtualization-based protection of code integrity](/windows/security/hardware-security/enable-virtualization-based-protection-of-code-integrity) for more information.
- Windows 11 Build 26100.2314 or later ***or*** Windows Server 2025 or later.

> [!WARNING]
> Ensure you have reviewed the OS support for VBS enclaves above, as support has recently changed.

## Development prerequisites

In addition to the device requirements, the following are required to develop VBS Enclaves:

- Visual Studio 2022 version 17.9 or later - The [Microsoft Visual C++ compiler (MSVC)](/cpp/build/reference/compiling-a-c-cpp-program) is required. Installing Visual Studio simplifies this.
- The [Windows Software Development Kit (SDK)](https://developer.microsoft.com/windows/downloads/windows-sdk/) version 10.0.22621.3233 or later, which provides `veiid.exe` (the VBS Enclave import ID binding utility) and `signtool.exe`.
- A [Trusted Signing](https://azure.microsoft.com/products/trusted-signing) account.

## Related content

- [VBS Enclaves development guide](vbs-enclaves-dev-guide.md)
- [APIs available in VBS enclaves](available-in-enclaves.md)
- [Securing your sensitive workloads with VBS Enclaves](https://aka.ms/VBSEnclavesBlog)
- [Secure Enclaves (Trusted Execution) overview](enclaves.md)
- [Always Encrypted with secure enclaves documentation](/azure/azure-sql/database/always-encrypted-with-secure-enclaves-landing)
- [Virtualization-based Security (VBS) | Windows Hardware Developer](/windows-hardware/design/device-experiences/oem-vbs)
- [New Windows 11 features strengthen security to address evolving cyberthreat landscape](https://www.microsoft.com/security/blog/2024/05/20/new-windows-11-features-strengthen-security-to-address-evolving-cyberthreat-landscape/)

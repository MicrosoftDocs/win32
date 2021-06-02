---
title: WFP API
description: The Windows Filtering Platform (WFP) API is divided into the following components.
ms.assetid: ff3f0d74-7e0b-4a3e-b66d-eaa61b89038a
ms.topic: article
ms.date: 05/31/2018
---

# WFP API

The Windows Filtering Platform (WFP) API is divided into the following components.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Component</th>
<th>Description</th>
<th>Header Files</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2"><a href="/windows-hardware/drivers/ddi/_netvista/">Callout API</a> (FWPS)${REMOVE}$<br />
</td>
<td><a href="/windows-hardware/drivers/ddi/_netvista/">Data types</a> used by callouts.<strong>Note</strong>  These data types are documented in the Microsoft Windows Driver Development Kit (DDK).<br/></td>
<td><dl> fwpstypes.h<br />
fwpstypes.idl<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="/windows-hardware/drivers/ddi/_netvista/">Functions</a> and <a href="/windows-hardware/drivers/ddi/_netvista/">enumerated types</a> used to implement callouts.<strong>Note</strong>  These functions and enumerated types are documented in the DDK.<br/></td>
<td><dl> fwpsu.h<br />
fwpsk.h<br />
</dl></td>

</tr>
<tr class="odd">
<td rowspan="2">IKE/AuthIP API (IKEEXT)${REMOVE}$<br />
</td>
<td><a href="fwp-enums.md">Enumerated types</a> and <a href="fwp-structs.md">structures</a> used for managing IKE and AuthIP main mode (MM) policy and security associations.</td>
<td><dl> iketypes.h<br />
iketypes.idl<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="fwp-ike-functions.md">Functions</a> used for managing IKE and AuthIP MM policy and security associations.</td>
<td><dl> fwpmu.h<br />
fwpmk.h<br />
</dl></td>

</tr>
<tr class="odd">
<td rowspan="2">IPsec API (IPSEC)${REMOVE}$<br />
</td>
<td><a href="fwp-enums.md">Enumerated types</a> and <a href="fwp-structs.md">structures</a> used for managing IPsec policies and security associations.</td>
<td><dl> ipsectypes.h<br />
ipsectypes.idl<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="fwp-ipsec-functions.md">Functions</a> used for managing IPsec policies and security associations.</td>
<td><dl> fwpmu.h<br />
fwpmk.h<br />
</dl></td>

</tr>
<tr class="odd">
<td rowspan="2">Management API (FWPM)${REMOVE}$<br />
</td>
<td><a href="fwp-enums.md">Enumerated types</a> and <a href="fwp-structs.md">structures</a> used for managing the filter engine.</td>
<td><dl> fwpmtypes.h<br />
fwpmtypes.idl<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="fwp-mgmt-functions.md">Functions</a> used for managing the filter engine. These functions are used to perform the following tasks:<br/>
<ul>
<li>Set and query filters, providers, and callouts.</li>
<li>Retrieve IPsec statistics.</li>
<li>Configure the Windows Filtering Platform.</li>
</ul></td>
<td><dl> fwpmu.h<br />
fwpmk.h<br />
</dl></td>

</tr>
<tr class="odd">
<td>Shared API (FWP)</td>
<td>Fundamental <a href="fwp-enums.md">enumerated types</a> and <a href="fwp-structs.md">structures</a> shared across the Windows Filtering Platform.</td>
<td><dl> fwptypes.h<br />
fwptypes.idl<br />
</dl></td>
</tr>
</tbody>
</table>



 

Data type names are all upper-case and underscore-delimited. The name always begins with a prefix that identifies its component group, such as [**FWPM\_PROVIDER0**](/windows/desktop/api/Fwpmtypes/ns-fwpmtypes-fwpm_provider0).

Function names are mixed-case and case-delimited. The name always begins with a prefix that identifies its component group, such as [**FwpmProviderContextAdd0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmprovidercontextadd0).

Most data and function names end with a version number. The fwpvi.h header file maps version-independent data and function names to the version that is appropriate for use with a given operating system. For more information, see [WFP Version-Independent Names and Targeting Specific Versions of Windows](wfp-version-independent-names-and-targeting-specific-versions-of-windows.md).

Each component does not stand alone. For example, IKE main mode (MM) policies are defined in the IKEEXT component, but are stored in a provider context and are associated with a filter both of which are found in the FWPM API component.

## User-Mode and Kernel-Mode Public Header Files

Most of the WFP functions can be called from either user mode or kernel mode. However, user-mode functions return a **DWORD** value that represents a Win32 error code, whereas kernel-mode functions return an **NTSTATUS** value that represents an NT status code. As a result, function names and semantics are identical between user mode and kernel mode, but function signatures are not. This requires separate user-mode and kernel-mode specific headers for the function prototypes. User-mode header file names end in "u" and kernel-mode header file names end in "k".

The following table lists the Win32 header files that define the WFP functions.

| Header Files | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fwpmk.h      | Kernel-mode function prototypes for FWPM, IPsec, and IKEEXT components. Available in the DDK only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| fwpmu.h      | User-mode function prototypes for FWPM, IPsec, and IKEEXT components. Available in the Microsoft Windows Software Development Kit (SDK) only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| fwpsk.h      | Kernel-mode function prototypes and enumerated types for FWPS component. Available in the DDK only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| fwpsu.h      | User-mode function prototypes and enumerated types for FWPS component. Available in the Windows SDK only.**Note**  The user-mode FWPS enumerated types are identical to the kernel-mode FWPS enumerated types. In consequence, these types are documented in the DDK only.<br/> **Note**  The user-mode FWPS function prototypes are identical to the kernel-mode FWPS function prototypes with the exception of the return code. User-mode FWPS functions return a **DWORD**, whereas kernel-mode FWPS functions return an **NTSTATUS**. In consequence, these functions are documented in the DDK only.<br/> |



 

All user-mode functions are exported from fwpuclnt.dll. All kernel-mode functions are exported from fwpkclnt.sys.

### Management (FWPM) and Callout (FWPS) Data Types

Most FWPM data types, which are used for management tasks such as adding filters or callouts from an application or driver, have FWPS counterparts. The FWPS data types are used during the actual filtering of network traffic, in the context of a callout routine for classification.

For example, in order to add a filter to a certain filtering engine layer, the programmer should use an FWPM type, like: `filter.layerKey = FWPM_LAYER_INBOUND_IPPACKET`. To check which layer a callout is being called from, the programmer should use the corresponding FWPS type: ` if (inFixedValues->layerId == FWPS_LAYER_INBOUND_IPPACKET)`.

Some FWPS counterparts to FWPM data types are expanding the original FWPM data types. For example, to add a filter condition at many filtering engine layers, the programmer specifies the `filterCondition.fieldKey = FWPM_CONDITION_IP_PROTOCOL` regardless of the filtering engine layer. To find a filter condition value, the programmer specifies a layer specific FWPS type, like: `inFixedValues->incomingValue[FWPS_FIELD_ALE_FLOW_ESTABLISHED_V4_IP_PROTOCOL]`.

The FWPS data types are generally smaller than their FWPM counterparts. For example, the [**FWPM filtering layer identifiers**](management-filtering-layer-identifiers-.md) are **GUID**s (16-bytes) whereas the [FWPS filtering layer identifiers](/windows-hardware/drivers/network/management-filtering-layer-identifiers) are **UINT16** (16-bits). The smaller size for FWPS data types improves system performance since integer comparisons outweigh **GUID** comparisons for real-time traffic. Also, the kernel memory is used efficiently since the FWPS types are all used in the kernel for managing the filters, whereas the FWPM types are stored in user-mode to manage the different layers.

## Related topics

<dl> <dt>

[WFP API Object Model](object-model.md)
</dt> <dt>

[WFP API Object Management](object-management.md)
</dt> </dl>


---
description: These examples for the HWREQCHK API demonstrates how it can be leveraged to determine Windows upgrade eligibility.
ms.assetid: c869d763-3771-4cbd-911c-f670a0bee4ab
title: HWREQCHK API examples
ms.topic: article
ms.date: 01/04/2023
---

# HWREQCHK API examples

> [!NOTE]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK). The earliest version in which these features appear is Windows Insider Preview, version 10.0.25289.

These examples for the HWREQCHK API demonstrates how it can be leveraged to get information about a hardware device and its determine Windows upgrade eligibility for specific versions of Windows 11 or later.

## GetHardwareRequirementSystemInfo API example

The example below demonstrates how to get the device system information by calling **GetHardwareRequirementSystemInfo**, which is the same information used by the Windows hardware requirement evaluation engine. The context is that it might be used by a "Can I upgrade?" tool to report the device system information that factored into the `true` or `false` response from the **EvaluateHardwareRequirement** function.

``` cpp
#include <windows.h>
#include <objbase.h>
#include <wil/resource.h>
#include <hwreqchkapi.h>
#define PRINT_TRUE_FALSE(cond) (cond ? L"TRUE" : L"FALSE")   

HRESULT
GetHardwareRequirementSystemInfoExample()
/*++
    Routine Description:
        Get the Hardware Requirements System Info that is used to evaluate against the requirements
    Example:
        Demonstrates GetHardwareRequirementSystemInfo API
    Arguments:
        N/A
    Return Value:
        HRESULT - S_OK or a FAILED HRESULT if unsuccessful getting the defined list of hardware requirements
--*/
{
    HWREQCHK_DEVICE_HARDWARE_SYSINFO sysinfo{};
    HRESULT result = GetHardwareRequirementSystemInfo(&sysinfo);
    if (SUCCEEDED(result))
    {
        wprintf(L"     SSE2 Processor Support: %ls\n", PRINT_TRUE_FALSE(sysinfo.SSE2ProcessorSupport));
        wprintf(L"       NX Processor Support: %ls\n", PRINT_TRUE_FALSE(sysinfo.NXProcessorSupport));
        wprintf(L"          PrefetchW Support: %ls\n", PRINT_TRUE_FALSE(sysinfo.PrefetchWSupport));
        wprintf(L" CompareExchange128 Support: %ls\n",
                                                PRINT_TRUE_FALSE(sysinfo.CompareExchange128Support));
        wprintf(L"           LahfSahf Support: %ls\n", PRINT_TRUE_FALSE(sysinfo.LahfSahfSupport));
        wprintf(L"             CPU Core Count: %lu\n", sysinfo.CpuCoreCount);
        wprintf(L"         SecureBoot Capable: %ls\n", PRINT_TRUE_FALSE(sysinfo.SecureBootCapable));
        wprintf(L"                TPM Version: %lu\n", sysinfo.TpmVersion   );
        wprintf(L"                    CPU Mhz: %lu\n", sysinfo.CpuMhz);
        wprintf(L"                      RamMB: %lu\n", sysinfo.RamMB);
        wprintf(L"           SystemDiskSizeMB: %lu\n", sysinfo.SystemDiskSizeMB);
        wprintf(L"               Architecture: %lu\n", sysinfo.Architecture);
        wprintf(L"                 CPU Vendor: %lu\n", sysinfo.CpuVendor      );
        wprintf(L"                 CPU Family: %lu\n", sysinfo.CpuFamily);
        wprintf(L"                  CPU Model: %lu\n", sysinfo.CpuModel);
        wprintf(L"               CPU Stepping: %lu\n", sysinfo.CpuStepping);
        wprintf(L"   ArmV81 Processor Support: %ls\n", PRINT_TRUE_FALSE(sysinfo.ArmV81ProcessorSupport));
        wprintf(L"                   Platform: %lu\n", sysinfo.Platform   );
        wprintf(L"                   IsServer: %ls\n", PRINT_TRUE_FALSE(sysinfo.IsServer  ));
        wprintf(L"              Lockdown Mode: %lu\n", sysinfo.LockdownMode);
        wprintf(L"                 Product OS: %lu\n", sysinfo.ProductOS  );
        wprintf(L"               Product Name: %ls\n", sysinfo.ProductName);
        wprintf(L"             Processor Name: %ls\n", sysinfo.ProcessorName);
    }
    else
    {
        wprintf(L"Failed calling GetHardwareRequirementSystemInfo. Error:0x%.8x\n", result);
    }
    return result;
}
```

## EvaluateHardwareRequirement API example

This example demonstrates the use of **EvaluateHardwareRequirement**. It is the function that queries device hardware system properties to evaluate against the defined hardware requirements. The example method, **EvaluateHardwareRequirementExample**, accepts a **HWREQCHK_DEVICE_HARDWARE_REQUIREMENT** structure that contains the information about which hardware requirement to evaluate against. The other examples will demonstrate different ways in which developers can fill in the contents of the structure to determine which requirement they want to evaluate against.

``` cpp
#include <windows.h>
#include <objbase.h>
#include <wil/resource.h>
#include <hwreqchkapi.h>

HRESULT
EvaluateHardwareRequirementExample(
    _In_ const HWREQCHK_DEVICE_HARDWARE_REQUIREMENT& deviceHardwareRequirement)
/*++
    Routine Description:
        Evaluate the specific hardware requirement using the information supplied in the HWREQCHK_DEVICE_HARDWARE_REQUIREMENT structure
    Example:
        Demonstrates EvaluateHardwareRequirement API
    Arguments:
        deviceHardwareRequirement - Specifies the specific device hardware requirement structure that is used to invoke the EvaluateHardwareRequirement API
    Return Value:
        HRESULT - S_OK or a Failed HRESULT if unsuccessful invoking the EvaluateHardwareRequirement API
--*/
{
    //
    // Automatically free HWREQCHK_DEVICE_HARDWARE_EVALUATION (via CoTaskMemFree) 
    // objects when it goes out of scope. See WIL (https://github.com/Microsoft/wil/wiki).
    //
    wil::unique_cotaskmem_array_ptr<HWREQCHK_DEVICE_HARDWARE_EVALUATION>
                                            deviceHardwareRequirementEvaluations;
    BOOL evaluationResult = FALSE;
    static const std::map<const std::wstring, const std::wstring> constraintRuleMapping =
    {
        { L"SSE2ProcessorSupport", L"Processor must support the SSE2 instruction set"} ,
        { L"NXProcessorSupport", L"Processor must support data execution prevention" },
        { L"CompareExchange128", L"Processor must support the CMPXCHG16B instruction also referred to as CompareExchange128" },
        { L"LahfSahfSupport", L"Processor must support the LAHF and SAHF instructions" },
        { L"PrefetchWSupport", L"Processor must support the PrefetchW instructions" },
        { L"CpuCores", L"The minimum number of CPU cores that must exist on the device" },
        { L"CpuFms", L"TPM must be version 2.0 exactly(no higher, no lower)" },
        { L"Tpm", L"TPM must be version 2.0 exactly" },
        { L"UefiSecureBoot", L"Secure boot must be supported on the device"},
        { L"Memory", L"The minimum amount of memory in MB that must exist on the device" },
        { L"IotMemory", L"The minimum amount of memory in MB that must exist on the device" },
        { L"ServerMemory", L"The minimum amount of memory in MB that must exist on the device" },
        { L"SystemDriveSize", L"The minimum amout of total system disk size" },
        { L"IotSystemDriveSize", L"The minimum amout of total system disk size" },
        { L"CpuFms", L"The CPU must be a supported Family, Model and Stepping (FMS) processor signature" },
        { L"BlockedByHomeSkuSModeStateSV", L"SMode must be disabled unless the OS SKU is a 'Home'SKU" }
    };

    HRESULT result = EvaluateHardwareRequirement(
        &deviceHardwareRequirement,
        &evaluationResult,
        &deviceHardwareRequirementEvaluations,
        deviceHardwareRequirementEvaluations.size_address<ULONG>());
    if (FAILED(result))
    {
        wprintf(L"The requirement failed the EvaluateHardwareRequirement API. Error:0x%.8x\n", result);
    }
    else
    {
        //
        // On Success, the 'evaluationResult' variable will either be TRUE (evaluation succeeded)
        // or it will be FALSE (evaluation failed).
        //
        if (evaluationResult != FALSE)
        {
            wprintf(L"The hardware requirement evaluation succeeded. The device does meet the hardware requirements\n");        
        }
        else
        {
            wprintf(L"The hardware requirement evaluation did not pass. The device does not meet the hardware requirements.\n");
        }

        // Loop through each constraint evaluation performed
        for (const auto& deviceHardwareRequirementEvaluation : deviceHardwareRequirementEvaluations)
        {    
            auto findConstraint = constraintRuleMapping.find(deviceHardwareRequirementEvaluation.RuleName);
            std::wstring constraintDescription = L"Constraint Not Found";
            if (findConstraint != constraintRuleMapping.end())
            {
                constraintDescription = findConstraint->second;
            }

            // Display the Rules that were evaluated as part of the requirements.
            // NOTE: RuleName is a non-localized value coming from the internally defined JSON contents.
            wprintf(L"\tConstraint Name: %-64ls Succeeded: %-8ls\n\t\tDescription: %ls\n",
                deviceHardwareRequirementEvaluation.RuleName,
                deviceHardwareRequirementEvaluation.Succeeded ? L"TRUE" : L"FALSE",
                constraintDescription.c_str());
        }

    if (evaluationResult == FALSE)
        {
            // The device failed to meet the hardware requirements, dump the system
            // info by calling the other example GetHardwareRequirementSystemInfoExample,
            // which calls the API GetHardwareRequirementSystemInfo and dumps the contents.
            GetHardwareRequirementSystemInfoExample();
        }
    }
    return result;
}
```

## GetLatestHardwareRequirement API example

The example below demonstrates the use of **GetLatestHardwareRequirement**. It's the function that queries and returns the latest hardware requirement for a given **HWREQCHK_PRODUCT_TYPE** enumeration value. If the call succeeds, it will then pass on the contents of the **HWREQCHK_DEVICE_HARDWARE_REQUIREMENT** structure to the **EvaluateHardwareRequirement** example above.

```cpp
#include <windows.h>
#include <objbase.h>
#include <wil/resource.h>
#include <hwreqchkapi.h>

HRESULT
GetLatestHardwareRequirementExample(
    _In_ HWREQCHK_PRODUCT_TYPE productType)
/*++
    Routine Description:
        Get the latest hardware requirement defined and then use 
        the information supplied in the HWREQCHK_DEVICE_HARDWARE_REQUIREMENT
        to evaluate hardware requirements against it.
    Example:
        Demonstrates the use of the GetLatestHardwareRequirement API. If successful, the
        EvaluateHardwareRequirementExample method is invoked to ‘evaluate’
        the latest hardware requirement.
    Arguments:
        productType - A valid HWREQCHK_PRODUCT_TYPE enumeration value to get the latest hardware requirement
    Return Value:
        HRESULT - S_OK or a FAILED HRESULT if unsuccessful getting the defined list of hardware requirements
--*/
{
    HWREQCHK_DEVICE_HARDWARE_REQUIREMENT deviceHardwareRequirement {};

    // Get the currently defined latest hardware requirement for the product type value
    // specified in the productEnum variable.
    HRESULT result = GetLatestHardwareRequirement(productType, &deviceHardwareRequirement);
    if (FAILED(result))
    {
        wprintf(L"The call to GetLatestHardwareRequirement failed. Error:0x%.8x\n", result);
    }
    else
    {
        // 
        // Use the default hardware requirement returned from the GetLatestHardwareRequirement API
        // to verify the hardware device requirements for the latest defined OS
        // by calling the EvaluateHardwareRequirementExample method.
        //
        result = EvaluateHardwareRequirementExample(deviceHardwareRequirement);
    }

    return result;
}
```

## GetHardwareRequirements API example

This example demonstrates the use of **GetHardwareRequirements** to get the entire list of hardware requirements that are defined and can be evaluated against. The example enumerates each of the requirements that are available until a specific requirement is found matching the arguments supplied to the example method.

```cpp
#include <windows.h>
#include <objbase.h>
#include <wil/resource.h>
#include <hwreqchkapi.h>

HRESULT
GetHardwareRequirementsExample(
    _In_ HWREQCHK_TARGET_RELEASE targetRelease,
    _In_ HWREQCHK_PRODUCT_TYPE productType)
/*++
    Routine Description:
        Gets all of the defined hardware requirements and evaluates one or more of the requirements
    Example:
        Demonstrates the use of the GetHardwareRequirements API. If successful and a
        match is found for the supplied requirement & product enum arguments, then the  
        EvaluateHardwareRequirementExample method is invoked to ‘evaluate’
        the hardware requirement.
    Arguments:
        targetRelease  - A valid HWREQCHK_TARGET_RELEASE enumeration value 
                         used to filter the list of returned requirement(s)
        productType    – A valid HWREQCHK_PRODUCT_TYPE enumeration value 
                         used to filter the list of returned requirement(s)
    Return Value:
        HRESULT        - S_OK or a FAILED HRESULT if unsuccessful getting the 
                         defined list of hardware requirements
--*/
{
    const HRESULT errNotFound = HRESULT_FROM_WIN32(ERROR_NOT_FOUND);

    //
    // Automatically free HWREQCHK_DEVICE_HARDWARE_REQUIREMENT (via CoTaskMemFree) 
    // objects when it goes out of scope. See WIL (https://github.com/Microsoft/wil/wiki).
    //
    wil::unique_cotaskmem_array_ptr<HWREQCHK_DEVICE_HARDWARE_REQUIREMENT> deviceHardwareRequirements;

    // Get the currently defined hardware requirements
    HRESULT result = GetHardwareRequirements(
                             &deviceHardwareRequirements, 
                             deviceHardwareRequirements.size_address<ULONG>());
    if (FAILED(result))
    {
        wprintf(L"The call to GetHardwareRequirements failed. Error:0x%.8x\n", result);
    }
    else
    {
        for (const auto& deviceHardwareRequirement : deviceHardwareRequirements)
        {
            result = errNotFound;

            // Look for a requirement matching the TargetRelease and ProductType enumeration values
            if (deviceHardwareRequirement.TargetRelease == targetRelease &&
                deviceHardwareRequirement.ProductType == productType)
            {
                // We found a match. Now evaluate the requirement by
                // calling the EvaluateHardwareRequirementExample method
                result = EvaluateHardwareRequirementExample(deviceHardwareRequirement);
                if (FAILED(result))
                {
                    wprintf(L"Error invoking the example method EvaluateHardwareRequirementExample\n");
                }
                break  ;
            }
        }
    }

    if (result == errNotFound  )
    {
        wprintf(L"Unable to locate a matching target-release '%d' and product-type '%d'\n",    
                targetRelease, producttype);
    }

    return result;
}
```

## Related topics

[HWREQCHK API overview](hwreqchk-overview.md)

[HWREQCHK API functions](hwreqchk-api-functions.md)

[Windows Implementation Libraries (WIL) wiki](https://github.com/Microsoft/wil/wiki)

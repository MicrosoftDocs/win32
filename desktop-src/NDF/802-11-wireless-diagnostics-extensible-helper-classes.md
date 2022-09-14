---
title: 802.11 Wireless Diagnostics Extensible Helper Classes
description: The built-in wireless diagnostics infrastructure has two extension points.Parent Helper ClassPurposeRevised Native Wifi (RNWF) Extensible Helper ClassDiagnoses issues related to 802.11 connectivity extensions.
ms.assetid: b54f836d-4fae-4e71-bf7b-af5a6e9e615c
ms.topic: article
ms.date: 05/31/2018
---

# 802.11 Wireless Diagnostics Extensible Helper Classes

The built-in wireless diagnostics infrastructure has two extension points.

| Parent Helper Class                                | Purpose                                                           |
|----------------------------------------------------|-------------------------------------------------------------------|
| Revised Native Wifi (RNWF) Extensible Helper Class | Diagnoses issues related to 802.11 connectivity extensions.       |
| L2Security Extensible Helper Class                 | Diagnoses issues related to Layer 2 security protocol extensions. |



 

> [!Note]  
> A third-party helper class should register with both parent helper classes to ensure that the third-party class gets called. For more information about registration, see [Registering NDF Helper Class Extensions](registering-ndf-helper-class-extensions.md).

 

## RNWF Extensible Helper Class

Parent Helper Class Name

``` syntax
Parent = L"RNWF Extensible Helper Class";
```

The Revised Native Wifi (RNWF) extensible helper class is the parent for third-party helper classes that diagnose issues related to extending 802.11 protocols used by Native Wifi.

The two key attributes provided by the RNWF helper class are the GUID of the interface where the issue occurred, and the connection context.

-   Interface GUID: This attribute is named "Interface ID" and is of type **AT\_GUID**.

-   Connection Context: This attribute is named Network ID and is of type AT\_OCTET\_STRING. This string is actually a buffer the WDIAG\_IHV\_WLAN\_ID structure defined in Wlanihv.h. This structure is defined as follows.

    ``` syntax
#define WDIAG_IHV_WLAN_ID_FLAG_SECURITY_ENABLED               0x00000001
    typedef
    struct _WDIAG_IHV_WLAN_ID
    {
        WCHAR                        strProfileName [MS_MAX_PROFILE_NAME_LENGTH];
        DOT11_SSID                   Ssid;
        DOT11_BSS_TYPE               BssType;
        DWORD                        dwFlags;           // Flags defined above
        DWORD                        dwReasonCode;      // Set only when an applicable reason code is available
    }
    WDIAG_IHV_WLAN_ID, *PWDIAG_IHV_WLAN_ID;
    ```

> [!Note]  
> **WDIAG\_IHV\_WLAN\_ID\_FLAG\_SECURITY\_ENABLED** is the only possible **dwFlags** value.

 

The matching attribute for the third-party helper class should be the same as its corresponding software module's service ID. This is also the same name the third-party should be registered in the registry. Wireless diagnostics will query the service ID during the wireless session in which the issue occurred. The information will be returned to NDF, which will determine whether the third-party helper class is present and registered, and then call it.

The following table lists the matching attributes for the RNWF extensible helper class.



| Name          | Type    | Value                         |
|---------------|---------|-------------------------------|
| DiagnosticsID | REG\_SZ | \[DiagnosticsID\_GUID\_String |



 

## L2Security Extensible Helper Class

Parent Helper Class Name

``` syntax
Parent = L"Extensible L2Sec Helper Class";
```

The Layer 2 Security (L2Security) extensible helper class is the parent for third-party helper classes that diagnose issues related to corresponding services and software modules that replace Layer 2 Security functionality.

The two key attributes provided by the Layer 2 Security helper class are the GUID of the interface where the issue occurred, and the connection context.

-   Interface GUID: This attribute is named "Interface ID" and is of type **AT\_GUID**.

-   Connection Context: This attribute is named Network ID and is of type AT\_OCTET\_STRING. This string is actually a buffer the WDIAG\_IHV\_WLAN\_ID structure defined in wlanihv.h. This structure is defined as follows.

    ``` syntax
#define WDIAG_IHV_WLAN_ID_FLAG_SECURITY_ENABLED               0x00000001
    typedef
    struct _WDIAG_IHV_WLAN_ID
    {
        WCHAR                        strProfileName [MS_MAX_PROFILE_NAME_LENGTH];
        DOT11_SSID                   Ssid;
        DOT11_BSS_TYPE               BssType;
        DWORD                        dwFlags;           // Flags defined above
        DWORD                        dwReasonCode;      // Set only when an applicable reason code is available
    }
    WDIAG_IHV_WLAN_ID, *PWDIAG_IHV_WLAN_ID;
    ```

> [!Note]  
> **WDIAG\_IHV\_WLAN\_ID\_FLAG\_SECURITY\_ENABLED** is the only possible **dwFlags** value.

 

The matching attribute for the third-party helper class should be the same as its corresponding software module's service ID. This is also the same name the third-party should be registered in the registry. Wireless diagnostics will query the service ID during the wireless session in which the issue occurred. The information will be returned to NDF, which will determine whether the third-party helper class is present and registered, and then call it.

The following table lists the matching attributes for the Layer 2 Security extensible helper class.



| Name          | Type    | Value                         |
|---------------|---------|-------------------------------|
| DiagnosticsID | REG\_SZ | \[DiagnosticsID\_GUID\_String |



 

## Matching Attributes

**DiagnosticsID**

802.11 Wireless Diagnostics will query the *DiagnosticsID* from the core Native Wifi service in order to find out if any third-party wireless extensions or security modules are installed and involved in the connection. Wireless Diagnostics will then provide hypotheses to these third-party helper classes using the *DiagnosticsID* as the matching attribute. Any third-party helper classes should be included in and installed with the associated driver package. The *DiagnosticsID* will be defined in the miniport INF file as a registry key in the [AddReg](https://msdn.microsoft.com/library/ms794514.aspx) directive.

``` syntax
HKR,Ndi\IHVExtensions, DiagnosticsID,0, "<Diagnostics ID GUID>"
```

This key defines the ID of the wireless helper class for the third-party software module. This key is optional for the extensibility framework, but it is needed if the implementation includes an IHV Wireless Helper Class that plugs into NDF and can diagnose connectivity problems related to the RNWF wireless or security extensions. MS WLAN diagnostics helper classes will query this ID from the Wireless Auto Configuration Service when IHV modules are installed and will provide this ID as the reference or matching attribute to NDF during a diagnostics session so that NDF can call the appropriate third-party wireless helper class when necessary.

**\[DiagnosticsID\_GUID\_String\]**

This value must be a string of all uppercase letters. For example, "{12345678-9ABC-DEF0-1234-56789ABCDEF0}".

## Scope of 802.11 Wireless Diagnostics Helper Classes

802.11 wireless diagnostics helper classes currently diagnose wireless issues in the following areas.

-   Any 802.11 connectivity issues including 802.11 association, 802.11 authentication, 802.11 security settings related to 802.11 standards & protocols natively supported in the operating system, and performance issues.
-   Layer 2 Security issues with regards to 802.1x configurations and any issues related to layer 2 authentication using methods natively supported on Windows Vista and Windows Server 2008.
-   Configuration mismatches in profile settings between the client and the Access Point or the network infrastructure and services.

802.11 wireless diagnostics helper classes currently do not diagnose wireless issues in the following areas.

-   Issues related to third-party 802.11 extensions including any profile or driver settings related to these extensions.
-   Issues related to third-party EAP methods.
-   Wireless miniport driver issues.
-   Any 802.11 and layer 2 security protocol or standards-related issues that are not natively supported.
-   System or component-level issues that might impact wireless connectivity, such as power management, low disk space, memory conditions, and hardware problems.

Additionally, 802.11 Wireless Diagnostics does not analyze [**HighUtilization**](/windows/desktop/api/ndhelper/nf-ndhelper-inetdiaghelper-highutilization) cases. Identified wireless performance issues will be analyzed and reported as [**LowHealth**](/windows/desktop/api/ndhelper/nf-ndhelper-inetdiaghelper-lowhealth) cases.

 

 





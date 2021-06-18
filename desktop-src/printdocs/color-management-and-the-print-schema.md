---
description: Learn about user configurable keywords in the Print Schema for color management, such as PageColorManagement and PageBlackGenerationProcessing.
ms.assetid: 296255b8-fe5c-46dd-b717-487aaae0db80
title: Color Management and the Print Schema
ms.topic: article
ms.date: 05/31/2018
---

# Color Management and the Print Schema

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

User Configurable Element keywords may either be XPS specific or non-XPS specific. In the case where they are not XPS specific, the keyword may be used for Legacy GDI-based printing. If an application decides to set these keywords in a PrintTicket, it is up to the driver to determine the proper action and behavior to take based on the definitions presented in the Print Schema. Any of these keywords may be used in the context of ICM. For more information, please see the Windows Vista SDK.



| Print Schema User Configurable Keyword       | DEVMODE Equivalent     | XPS Specific   |
|----------------------------------------------|------------------------|----------------|
| PageColorManagement<br/>               | dmICMMethod<br/> | No<br/>  |
| PageBlackGenerationProcessing<br/>     | None<br/>        | Yes<br/> |
| PageBlendColorSpace<br/>               | None<br/>        | Yes<br/> |
| PageSourceColorProfile<br/>            | None<br/>        | No<br/>  |
| PageDestinationColorProfile<br/>       | None<br/>        | No<br/>  |
| PageICMRenderingIntent<br/>            | dmICMIntent<br/> | No<br/>  |
| JobOptimalDestinationColorProfile<br/> | None<br/>        | No<br/>  |
| PageDeviceColorSpaceUsage<br/>         | None<br/>        | Yes<br/> |



 

## PageColorManagement System Handling

For PageColorManagement, the system provides automatic handling of PrintTicket to DEVMODE or DEVMODE to PrintTicket conversion if necessary. This depends on the specific print path between the application (Win32 or WPF)and the driver (GDI-based or XPSDrv). In the case of printing from a Windows Presentation Foundation application to a Microsoft XPSDrv print driver, a PageColorManagement public option of System SHOULD NOT be advertised in either the PrintTicket or PrintCapabilities document; in this case, color management cannot be handled automatically by the system. Printing from a Win32 application to a Microsoft XPSDrv print driver may result in color management between the application and GDI, however after conversion to XPS-format, there will be no automatic system handling of color management between the XPS document and the driver and/or device, because the XPS-format tags each element with complete color information, and it is up to the driver or the device to process this information.



| PageColorManagement Public Options | DEVMODE Value                  |
|------------------------------------|--------------------------------|
| None<br/>                    | DMICMMETHOD\_NONE<br/>   |
| Device<br/>                  | DMICMMETHOD\_DEVICE<br/> |
| Driver<br/>                  | DMICMMETHOD\_DRIVER<br/> |
| System<br/>                  | DMICMMETHOD\_SYSTEM<br/> |



 

## PageICMRenderingIntent System Handling

For PageICMRenderingIntent, the system provides automatic handling of PrintTicket to DEVMODE or DEVMODE to PrintTicket conversion if necessary. This depends on the specific print path between the application (Win32 or Windows Presentation Foundation) and the driver (GDI-based or XPSDrv).



| PageICMRenderingIntent Public Options | DEVMODE Value                       |
|---------------------------------------|-------------------------------------|
| AbsoluteColorimetric<br/>       | DMICM\_ABS\_COLORIMETRIC<br/> |
| RelativeColorimetric<br/>       | DMICM\_COLORIMETRIC<br/>      |
| Photographs<br/>                | DMICM\_CONTRAST<br/>          |
| BusinessGraphics<br/>           | DMICM\_SATURATE<br/>          |



 

All other Color Management related keywords (besides PageColorManagement or PageICMRenderingIntent) do not have such automatic handling.

## JobOptimalDestinationColorProfile and PageDestinationColorProfile Usage

An application MAY decide to query PrintCapabilities document for JobOptimalDestinationColorProfile. This could give an application the optimal color profile given the current device configuration as defined in the PrintCapabilities document. If the application decides it would like the driver to perform color management to the destination color profile specified by JobOptimalDestinationColorProfile, then PageColorManagement and PageDestinationColorProfile would be set to Driver and DriverConfiguration in the PrintTicket respectively. If the application does not want to use the JobOptionalDestinationColorProfile and chooses to use its own, it SHOULD set PageColorManagement to None and also set the PageDestinationColorProfile to Application in the PrintTicket to convey that the application has already performed color management to its specified destination color profile. Another scenario may occur when the application chooses to use the optimal destination color profile returned by the drivers PrintCapabilities but decides to do color management on its own. In this case, PageColorManagement would be set to None and PageDestinationColorProfile would be set to Application.

## PageSourceColorProfile Usage

For PageSourceColorProfile, an application MAY specify a source color profile for each page in the PrintTicket, regardless of the option selected for PageColorManagement. Whether it is present or not, it is up to the driver to decide the behavior for each case based on the definitions presented in the Print Schema. For example, an application may set PageColorManagement to None, and then not set PageSourceColorProfile in the PrintTicket. It is also possible for an application to set PageColorManagement to Driver, and then set PageSourceColorProfile in the PrintTicket; the driver in this case is responsible for determining the behavior within the guidelines of the PrintSchema.

## PageDeviceColorSpaceUsage

PageDeviceColorSpaceUsage is an XPS specific user configurable element that is set by the application. It provides instructions for the device by setting the appropriate option in the PrintTicket, for color space profile handling associated within an XPS document. The application and/or existing PrintTicket MAY specify this keyword in a PrintTicket sent to the device. Whether it is present or not, it is up to the driver to decide the behavior for each case, based on the definitions presented in the Print Schema.

## Print Schema Color Management Example Flow

The following diagram illustrates flow for the most likely scenarios for using Color Management and the Print Schema. For simplicity and readability, only the following user configurable Print Schema keywords were used to demonstrate their usage: PageColorManagement, JobOptimalDestinaionColorProfile, PageSourceColorProfile, and PageDestinationColorProfile. A solid line represents an action that SHOULD occur and a dashed line represents an action that MAY occur. The following scenario is not the guaranteed interaction that will result between the application, driver, and system, however, it represents the most common usage case that will occur.

![a diagram that shows how color management settings are processed](images/local-1992284846-colormanagementtest3.png)

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 





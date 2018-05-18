---
title: How-to enable email notification
description: Email notification allows for a protected content owner to be notified when his or her content is accessed.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '5FB975EE-E4E5-4089-B8E1-CAFD5B9B34EC'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
---

# How-to: enable email notification

Email notification allows for a protected content owner to be notified when his or her content is accessed.

To setup your email notification for a given license, use [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md) with the property type parameter, *dwPropID*, as [**IPC\_LI\_APP\_SPECIFIC\_DATA**](license-property-types.md) and the application data fields formatted as an [**IPC\_NAME\_VALUE\_LIST**](ipc-name-value-list.md).


```C++
...

int numDataPairs = 3;

IPC_NAME_VALUE propertyValuePairs [numDataPairs];

// lcid field set to 0 causes the default lcid to be used

propertyValuePairs[0] = {"MS.Conetent.Name", 0, "FinancialReport.docx"};
propertyValuePairs[1] = {"MS.Notify.Enabled",0 , "true"};
propertyValuePairs[2] = {"MS.Notify.Culture",0 , “en-US”};

IPC_NAME_VALUE_LIST emailNotificationAppData = {numDataPairs, propertyValuePairs};

result = IpcSetLicenseProperty( licenseHandle, FALSE, IPC_LI_APP_SPECIFIC_DATA, emailNotificationAppData);

...
```



The following table contains the application data fields, property name and value pairs, for RMS email notification.



| Property name                | Data type             | Example value                      | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------------------------|-----------------------|------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MS.Content.Name<br/>   | **string**<br/> | “FinancialReport.docx”<br/>  | This is an identifier associated with the protected content.<br/> For protected files this value should be the name of the file without any path information.<br/> For other types of content such as an email message it might be the subject of the email or it might be empty.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| MS.Notify.Enabled<br/> | **string**<br/> | “true” \| “false”<br/>       | If this value is set to “true” a notification email will be sent to the owner of the publishing license when someone attempts to use it to obtain an end user license.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| MS.Notify.Culture<br/> | **string**<br/> | “en-US”<br/>                 | **Source:** System.Globalization.CultureInfo.CurrentUICulture.Name<br/> This value is used to determine the localized language of the notification email and the date/time and number formatting that should be used in the email message.<br/> It should be set based on user settings of the machine that the publish license is created on, or based on the preferred culture of the owner of the publish license.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| MS.Notify.TZID<br/>    | **string**<br/> | “Pacific Standard Time”<br/> | **Source:** TimeZoneInfo.Local.Id - Windows time zone ID.<br/> This value is the Microsoft Windows OS time zone identifier describing a particular time zone and its characteristics.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| MS.Notify.TZO<br/>     | **string**<br/> | “-480”<br/>                  | This is the publish license owner’s time zone offset in terms of minutes from UTC time.<br/> If a valid TZID value is provided the offset of the time zone specified by it will be used and this value will be ignored.<br/> This value will more than likely be used by non-windows based publishing platforms that do not have access to the list of Windows OS time zone ID values.<br/> If a TZID value is not provided this value will be used to calculate the time offset in notification messages, and the TZSN will be used (regardless of the time zone value) to indicate the name of the time zone. This will result time zone being fixed and not updating for daylight savings when it is applicable.<br/> For example:<br/> If TXID is blank and TZ0 is set to “-420” and the TZSN is set to “Pacific Daylight Time” all values shown in the notification email will be adjusted to "Pacific Daylight Time" and displayed as such even if daylight savings is no longer in affect currently.<br/> On the other hand if a TZID is supplied along with both TZSN and TZDN, then the times specified in the notification email will be adjusted and displayed based on whether the date and time should be displayed in Daylight mode or Standard mode.<br/> |
| MS.Notify.TZSN<br/>    | **string**<br/> | “Pacific Standard Time”<br/> | **Source:** TimeZoneInfo.Local.StandardName - Standard Time Zone name.<br/> This should the localized name of the time zone’s standard time zone name.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| MS.Notify.TZDN<br/>    | **string**<br/> | “Pacific Daylight Time”<br/> | **Source:** TimeZoneInfo.Local.DaylightName - Daylight Time Zone name.<br/> This should be the localized name of the time zone’s daylight savings name. It can be the same as the standard name if the time zone does not support daylight savings.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |



 

## Related topics

<dl> <dt>

[**IpcSetLicenseProperty**](ipcsetlicenseproperty.md)
</dt> <dt>

[**IPC\_LI\_APP\_SPECIFIC\_DATA**](license-property-types.md)
</dt> <dt>

[**IPC\_NAME\_VALUE\_LIST**](ipc-name-value-list.md)
</dt> </dl>

 

 






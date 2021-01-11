---
description: HKCU\\Control Panel\\International.
ms.assetid: e2925d92-19df-42e5-9893-2820f437d3a5
title: AddHijriDate
ms.topic: article
ms.date: 05/31/2018
---

# AddHijriDate

**HKCU\\Control Panel\\International**



| Data type | Range                      | Default value |
|-----------|----------------------------|---------------|
| REG\_SZ   | *A valid adjustment value* | (None)        |



 

## Description

Specifies adjustments to the date within the Hijri calendar.

The Hijri calendar is a lunar calendar used in the Islamic world. The months begin and end according to a decree that is based on the observation of the new moon. It is difficult to accurately predict the beginnings and endings of the months, and there are regional variations, so an adjustment of between zero and two days is made to the calendar.

The **AddHijriDate** registry value stores this adjustment value as follows.



| Value          | Meaning                                                                                                                                                                                                                               |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AddHijriDate-2 | Subtract two days.                                                                                                                                                                                                                    |
| AddHijriDate   | Subtract one day.                                                                                                                                                                                                                     |
| (blank)        | No adjustment is necessary. (If the date has not been adjusted, this entry does not appear in the registry. If the date has been adjusted and then restored to its original value, this entry appears in the registry with no value.) |
| AddHijriDate+1 | Add one day.                                                                                                                                                                                                                          |
| AddHijriDate+2 | Add two days.                                                                                                                                                                                                                         |



 

This entry does not exist in the registry by default. You can add it by using the registry editor Regedit.exe or by using the change method described below.

## Change Method

To change the value of this entry, or to add it to the registry, first install the files for complex script and right-to-left languages. In Control Panel, click **Regional and Language Options**, then click the **Languages** tab. Under **Supplemental language support**, select the checkbox to **Install files for complex script and right-to-left languages (including Thai)**. Click **OK**.

To change the value of this entry, or to add it to the registry, from Control Panel, click **Regional and Language Options**. In the **Standards and Formats** field, select a locale that uses the Hijri calendar. Click the **Customize** button, then click the **Date** tab. In the **Adjust Hijri date to:** drop-down list, select the appropriate value. Click **OK**, then click **OK** again.

## Activation Method

Changes to this entry made through Control Panel take effect immediately.

 

 




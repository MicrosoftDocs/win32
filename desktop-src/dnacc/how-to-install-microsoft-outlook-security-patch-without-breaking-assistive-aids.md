---
Description: Microsoft Corporation
ms.assetid: '4c37e7cd-5c21-46a0-94a7-fe2c8627c30a'
title: How To Install Microsoft Outlook Security Update Without Breaking Assistive Aids
---

# How To Install Microsoft Outlook Security Update Without Breaking Assistive Aids

Microsoft Corporation

September 2001

**Summary:** The following document describes how installing a security update for Microsoft Outlook 98 and Outlook 2000 can affect certain accessibility functionalities. (1 printed page)

Viruses that spread through email do so by using the Contacts list and Address Book in Outlook. By using Outlook automation (by means of the extensible object model in Outlook), the virus forwards itself to all contacts. The Outlook 98/2000 Email Security Update prevents mail from being sent without your permission and protects you from accidentally opening attached files that may pose a security risk to your computer. However, in providing a higher level of security, this update limits certain Outlook functionality.

Certain functionalities in assistive aids can be broken as a result. In particular, the update blocks out the **accDoDefaultAction** Active Accessibility method of the **Send** button and the **File Send** menu item. Voice input utilities, onscreen keyboards or switch devices, for example, are unable to act on these objects by means of Active Accessibility.

The solution is to map the command to key sequences that achieve the same purpose. Although the **accDoDefaultAction** method is blocked, pressing ALT+S, CTRL+ENTER, ALT+F, E and ENTER on the **File Send** menu item will continue to work. Assistive aids can map their send commands to these key sequences.

The blocked `accDoDefaultAction` behavior can be demonstrated using the Inspect tool available in the [Microsoft Windows SDK](http://go.microsoft.com/fwlink/p/?linkid=208210).

 

 




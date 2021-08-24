---
title: Calling WDS from Web Pages
description: You can call Microsoft Windows Desktop Search (WDS) from any webpage you create or maintain using the Browser Helper Object (BHO) and Windows Internet Explorer.
ms.assetid: 8d9fa541-530e-4917-a6d9-4e04549ce32e
ms.topic: article
ms.date: 05/31/2018
---

# Calling WDS from Web Pages

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use [Windows Search](../search/-search-3x-wds-overview.md) instead.

You can call Microsoft Windows Desktop Search (WDS) from any webpage you create or maintain using the Browser Helper Object (BHO) and Windows Internet Explorer. You can see how this works on the MSN webpage. Above the search box on https://www.msn.com are several search types: Web, News, Images, Desktop, Encarta, and Local. If you click Desktop, the search parameters are passed to Windows Desktop Search, which searches the catalog and displays results in the WDS user interface. For users to start a desktop search from your webpage(s), the WDSBHO must be installed and enabled on their systems, your webpage(s) must be registered with WDS as an allowed URL, and you must create a link to pass the user-enetered query to WDS.

## Enabling the WDS Browser Help Object

The BHO is installed and enabled within Internet Explorer by default when you install WDS, but you can easily verify that it hasn't been disabled or uninstalled. On a user's system, open Internet Explorer , select **Internet Options** from the **Tools** menu, click the **Programs** tab, and then click **Manage Add-Ons**. In your list of add-ons, look for the dsWebAllowBHO Class and make sure it is enabled. When the BHO is disabled, WDS will continue to work normally; however, you will not be able to search the desktop from a webpage.

Both of the following options for allowing a desktop search will execute the search locally with the registered search application.

## Registering Web Page URLs

The Registry includes a list of "allowed" domain URLs from which WDS can be called. To include your webpage(s), you need to list your domain URL(s) as REG\_SZ in the Registry as follows:

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**Windows Desktop Search**\\**DSW**\\**Allowed**\\*&lt;number&gt;* = &lt;domainURL&gt;

Where **&lt;number&gt;** is sequentially numbered, and **&lt;domainURL&gt;** is the URL of the Web Page you want to allow WDS searches from. This URL string can include the wildcard asterisk \* at the beginning or end of the URL. For example, if the string is "\*.mydomain.com", then you can start a WDS search from both https://www.mydomain.com and https://mydomain.com.

## Enabling Desktop Search by URL

Another option that does not require access to the Registry is to use the following URL on your webpage(s):

https://toolbar.msn.com/desktop/results.aspx?q=QUERY

where **QUERY** is the URL-encoded string the user is searching on, including any [Advanced Query Syntax](-search-2x-wds-aqsreference.md) terms.

 

 





---
title: query
description: Displays trace and providers query options.
ms.assetid: '80017d5d-21b8-450d-931b-0e8b7ef398f3'
keywords: ["query Windows Performance Analyzer"]
topic_type:
- apiref
api_name:
- query
api_type:
- NA
---

# query

Displays trace and providers query options.

``` syntax
xperf {-Providers [options] | -Loggers | -BootTrace | -ProfInt}
```

## Parameters

<dl> <dt>

<span id="_______-Providers___options...______"></span><span id="_______-providers___options...______"></span><span id="_______-PROVIDERS___OPTIONS...______"></span> **-Providers \[***options***...\]** 
</dt> <dd>

Query all installed/known and registered providers, as well as all known kernel flags and groups. For details, please see "xperf -help providers".

</dd> <dt>

<span id="_______-Loggers___________________________"></span><span id="_______-loggers___________________________"></span><span id="_______-LOGGERS___________________________"></span> **-Loggers** 
</dt> <dd>

Query all active logging sessions.

</dd> <dt>

<span id="_______-BootTrace_______"></span><span id="_______-boottrace_______"></span><span id="_______-BOOTTRACE_______"></span> **-BootTrace** 
</dt> <dd>

Query the boot trace configuration.

</dd> <dt>

<span id="_______-ProfInt______"></span><span id="_______-profint______"></span><span id="_______-PROFINT______"></span> **-ProfInt** 
</dt> <dd>

Query the current profile interval.

</dd> <dt>

<span id="_______-Profiles__ProfileFileName___ProfileName_______"></span><span id="_______-profiles__profilefilename___profilename_______"></span><span id="_______-PROFILES__PROFILEFILENAME___PROFILENAME_______"></span> **-Profiles** {*ProfileFileName* \| *ProfileName*} 
</dt> <dd>

Query the profile names defined in ProfileFileName or the ProfileName options. If no parameters are specified, query the names of the built-in profiles.

</dd> <dt>

<span id="_______-ProfilesWithDetails__ProfileFileName___ProfileName_______"></span><span id="_______-profileswithdetails__profilefilename___profilename_______"></span><span id="_______-PROFILESWITHDETAILS__PROFILEFILENAME___PROFILENAME_______"></span> **-ProfilesWithDetails** {*ProfileFileName* \| *ProfileName*} 
</dt> <dd>

Query the profile names defined in ProfileFileName or detailed properties in the ProfileName options. If no parameters are specified, query the names of the built-in profiles.

</dd> <dt>

<span id="_______-ProfileSessions__ProfileFileName___SessionName_______"></span><span id="_______-profilesessions__profilefilename___sessionname_______"></span><span id="_______-PROFILESESSIONS__PROFILEFILENAME___SESSIONNAME_______"></span> **-ProfileSessions** {*ProfileFileName* \| *SessionName*} 
</dt> <dd>

Query the profile session names defined in ProfileFileName or the SessionName properties. If no parameters are specified, query the names of the builtin profile sessions.

</dd> <dt>

<span id="_______-ProfileProviders__ProfileFileName___ProviderName_______"></span><span id="_______-profileproviders__profilefilename___providername_______"></span><span id="_______-PROFILEPROVIDERS__PROFILEFILENAME___PROVIDERNAME_______"></span> **-ProfileProviders** {*ProfileFileName* \| *ProviderName*} 
</dt> <dd>

Query the profile provider names defined in ProfileFileName or the ProviderName properties. If no parameters are specified, query the names of the builtin profileproviders.

</dd> <dt>

<span id="_______-ProfileLoggers________ProfileName______"></span><span id="_______-profileloggers________profilename______"></span><span id="_______-PROFILELOGGERS________PROFILENAME______"></span> **-ProfileLoggers** *ProfileName* 
</dt> <dd>

Query logging sessions specified in profile ProfileName.

</dd> </dl>

 

 





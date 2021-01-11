---
description: The SetReg tool sets the value of the registry keys that control the behavior of the Authenticode certificate verification process.
ms.assetid: 6c456a59-ee6c-420d-b075-7de8bd2fd8ff
title: SetReg
ms.topic: article
ms.date: 05/31/2018
---

# SetReg

The SetReg tool sets the value of the registry keys that control the behavior of the Authenticode certificate verification process. These keys are called the Software Publishing State Keys. After completing the requested action, the tool displays the current state of the Software Publishing State Keys.

**SetReg** \[*Options*\] \[*Choice \#* {**TRUE**\|**FALSE**}\]

The Set Registry tool only ships with the .NET Framework SDK version 1.0 and .1.1, which you can download from the [Microsoft Download Center](https://www.microsoft.com/download/details.aspx?id=16217).

## Options

The options can be one of the following values. Options given in the following table can be used only with Internet Explorer 4.0 or later.



| Option | Description                                                                                                                                            |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| **-q** | Suppress the display of the Software Publishing State Key values after SetReg has completed the requested action. The values are displayed by default. |
| **-?** | List command syntax and options.                                                                                                                       |



 

## Choice \#

*Choice \#* must be one of the following values.



| Choice | Description                                                                                                                       | Result                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **1**  | Trust the Test Root                                                                                                               | This value is ignored.**Windows XP/2000:** If **TRUE**, trusts a test root. This is equivalent to running "regedit wvtston.reg" in Internet Explorer 3.*x*.<br/> The default is **FALSE**. Any file signed with a test root will not verify unless this flag is set to **TRUE**. Note that this behavior has changed with Windows XP with Service Pack 1 (SP1) because Windows XP with SP1 ignores this value.<br/> <br/> |
| **2**  | Use expiration date on certificates                                                                                               | If **TRUE**, checks the certificate expiration date. To ignore expiration dates, set this flag to **FALSE**. The default is **TRUE**.                                                                                                                                                                                                                                                                                                       |
| **3**  | Check the [*revocation list*](../secgloss/c-gly.md) | If **TRUE**, performs the revocation check. To bypass revocation check, set this flag to **FALSE**. The default is **TRUE**.**Internet Explorer 3.*x*:** The default is **FALSE**.<br/>                                                                                                                                                                                                                                               |
| **4**  | Offline Revocation server OK (Individual)<br/>                                                                              | If **TRUE**, allows offline approval for individual certificates. The default is **FALSE**.                                                                                                                                                                                                                                                                                                                                                 |
| **5**  | Offline Revocation server OK (Commercial)<br/>                                                                              | If **TRUE**, allows offline approval for commercial certificates. The default is **TRUE**.                                                                                                                                                                                                                                                                                                                                                  |
| **6**  | Java offline Revocation server OK (Individual)<br/>                                                                         | If **TRUE**, allows offline approval for individual certificates and does not display the user interface for bad certificates. The default is **FALSE**.                                                                                                                                                                                                                                                                                    |
| **7**  | Java offline Revocation server OK (Commercial)<br/>                                                                         | If **TRUE**, allows offline approval for commercial certificates and does not display the user interface for bad certificates. The default is **TRUE**.                                                                                                                                                                                                                                                                                     |
| **8**  | Make version 1 signed objects no longer valid                                                                                     | If **TRUE**, makes version 1 signed objects no longer valid. The default is **FALSE**.                                                                                                                                                                                                                                                                                                                                                      |
| **9**  | Check the revocation list of the time stamp server                                                                                | If **TRUE**, performs the revocation check on the time stamp server's certificate. The default is **FALSE**.**Internet Explorer 3.*x*:** This value is not supported.<br/>                                                                                                                                                                                                                                                            |
| **10** | Only trust items found in the Trust database                                                                                      | If **TRUE**, allows downloads from publishers that are contained in the Personal Trust Database. The default is **FALSE**. **Internet Explorer 3.*x*:** This value is not supported.<br/>                                                                                                                                                                                                                                             |



 

 

 

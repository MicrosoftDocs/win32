---
description: Must retrieve configuration information from the security database and the service, compare the two sets of information, and then update the analysis section of the security database with any differences.
ms.assetid: f8420dde-55a2-40a0-b10d-140c28c0e9e4
title: Implementing SceSvcAttachmentAnalyze
ms.topic: article
ms.date: 05/31/2018
---

# Implementing SceSvcAttachmentAnalyze

The [**SceSvcAttachmentAnalyze**](scesvcattachmentanalyze.md) function must retrieve configuration information from the security database and the service, compare the two sets of information, and then update the analysis section of the security database with any differences. You can ensure this by using the following algorithm.

**To implement SceSvcAttachmentAnalyze**

1.  Define the variables needed to retrieve and set the security information and return codes.
2.  Call the pfQueryInfo callback function in the callback structure to retrieve configuration information from the security database.
3.  Retrieve the corresponding information from the service.
4.  Compare the configuration data retrieved from the service with that retrieved from the security database.
5.  If the information is not the same, call the pfSetInfo callback function in the callback structure to update the database.
6.  Free all buffers used to retrieve information. Call the pfFreeInfo callback function in the callback structure to free memory used for returned database information.
7.  If there is any message that the extension wants to add to the analysis log file, call the pfLogInfo callback function in the callback structure.
8.  Return the appropriate **SCESTATUS** codes.

The following example shows one possible implementation of [**SceSvcAttachmentAnalyze**](scesvcattachmentanalyze.md). Note that in this example, the functions QueryConfigurationLine and CompareValue respectively query information from the service and compare those values with those retrieved from the security database. The implementation of these functions is not shown.


```C++
#include <windows.h>

SCESTATUS WINAPI SceSvcAttachmentAnalyze (
    IN PSCESVC_CALLBACK_INFO pSceCbInfo
)
{
  
    ////////////////////////////////////////////////////
    // Define variables.
    ////////////////////////////////////////////////////
    PSCESVC_CONFIGURATION_INFO     pConfigInfo = NULL;
    SCESTATUS                      retCode;
    SCE_ENUMERATION_CONTEXT        EnumContext = 0;
  
  

    if ( pSceCbInfo == NULL ||
         pSceCbInfo->sceHandle == NULL ||
         pSceCbInfo->pfQueryInfo == NULL ||
         pSceCbInfo->pfSetInfo == NULL ||
         pSceCbInfo->pfFreeInfo == NULL ) 
    {
        return(SCESTATUS_INVALID_PARAMETER);
    }


  ////////////////////////////////////////////////////
  // Retrieve information from security database.
  ///////////////////////////////////////////////////
    do
    {
        retCode =  (*(pSceCbInfo->pfQueryInfo))(
                              pSceCbInfo->sceHandle,
                              SceSvcConfigurationInfo,
                              NULL,
                              FALSE,
                              &pConfigInfo,
                              &EnumContext
                              );
        if(retCode == SCESTATUS_SUCCESS && pConfigInfo != NULL)
        {
          ULONG i;
          for(i = 0;i < pConfigInfo->Count; i++)
          {
            if(pConfigInfo->Line[I].Key == NULL) 
                continue;
        
        //////////////////////////////////////////////
        // Query service for corresponding key.
        //////////////////////////////////////////////
            QueryConfigurationLine(
                               pConfigInfo->Line[i].Key,
                               &SystemValue);
        
        //////////////////////////////////////////////
        // Compare values.
        //////////////////////////////////////////////
            CompareValue(
                     pConfigInfo->Line[i].Key,
                     SystemValue,
                     pConfigInfo->Line[i].Value,
                     &Result);
        
        //////////////////////////////////////////////
        // Write to security database if values are 
        // not equal.
        //////////////////////////////////////////////
            if(Result != NULL)
            {
              retCode =  (*(pSceCbInfo->pfSetInfo))(pSceCbInfo->sceHandle,
                                      SceSvcAnalysisInfo,
                                      pConfigInfo->Line[i].Key,
                                      TRUE,
                                      Result);
              if(retCode != SCESTATUS_SUCCESS)
              {
                //////////////////////////////////////////
                // Add code to handle other return codes.
                //////////////////////////////////////////
              }
            }
        }
      
          //////////////////////////////////////////////
          // Free all buffers used to retrieve 
          // SceSvcFree frees memory allocated by call 
          // to SceSvcQueryQueryInfo. 
          /////////////////////////////////////////
        (*(pSceCbInfo->pfFreeInfo)) (PVOID)pConfigInfo);
          pConfigInfo = NULL;
    }
  } while (retCode == SCESTATUS_SUCCESS && pConfigInfo != NULL);
  
  
  //////////////////////////////////////////////////
  // If the return code is not SCESTATUS_SUCCESS, add code to 
  // set error message appropriately.
  //////////////////////////////////////////////////
  return retCode;
}
```



 

 




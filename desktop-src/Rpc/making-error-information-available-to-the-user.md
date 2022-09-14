---
title: Making Error Information Available to the User
description: When a caller receives an error and needs to notify the user of the error, the presence of extended error information should be checked, and if found, the caller should make the resulting information available to the user.
ms.assetid: 18689280-7124-46e4-9341-ad8d0c1705db
ms.topic: article
ms.date: 05/31/2018
---

# Making Error Information Available to the User

When a caller receives an error and needs to notify the user of the error, the presence of extended error information should be checked, and if found, the caller should make the resulting information available to the user. The following code fragment is an example of making this information available to the user:


```C++
// Make an API
status = //...
if (status)
    {
    RPC_STATUS Status2;
    RPC_ERROR_ENUM_HANDLE EnumHandle;

    Status2 = RpcErrorStartEnumeration(&EnumHandle);
    if (Status2 == RPC_S_ENTRY_NOT_FOUND)
        {
        //...
        }
    else if (Status2 != RPC_S_OK)
        {
        PrintToConsole("Couldn't get EEInfo: %d\n", Status2);
        //...
        }
    else
        {
        RPC_EXTENDED_ERROR_INFO ErrorInfo;
        int Records;
        BOOL Result;
        BOOL CopyStrings = TRUE;
        BOOL fUseFileTime = TRUE;
        SYSTEMTIME *SystemTimeToUse;
        SYSTEMTIME SystemTimeBuffer;

        while (Status2 == RPC_S_OK)
            {
            ErrorInfo.Version = RPC_EEINFO_VERSION;
            ErrorInfo.Flags = 0;
            ErrorInfo.NumberOfParameters = 4;
            if (fUseFileTime)
                {
                ErrorInfo.Flags |= EEInfoUseFileTime;
                }

            Status2 = RpcErrorGetNextRecord(&EnumHandle, CopyStrings, &ErrorInfo);
            if (Status2 == RPC_S_ENTRY_NOT_FOUND)
                {
                break;
                }
            else if (Status2 != RPC_S_OK)
                {
                PrintToConsole("Couldn't finish enumeration: %d\n", Status2);
                break;
                }
            else
                {
                int i;

                if (ErrorInfo.ComputerName)
                    {
                    PrintToConsole("ComputerName is %S\n", ErrorInfo.ComputerName);
                    if (CopyStrings)
                        {
                        Result = HeapFree(GetProcessHeap(), 0, ErrorInfo.ComputerName);
                        ASSERT(Result);
                        }
                    }
                PrintToConsole("ProcessID is %d\n", ErrorInfo.ProcessID);
                if (fUseFileTime)
                    {
                    Result = FileTimeToSystemTime(&ErrorInfo.u.FileTime, 
                        &SystemTimeBuffer);
                    ASSERT(Result);
                    SystemTimeToUse = &SystemTimeBuffer;
                    }
                else
                    SystemTimeToUse = &ErrorInfo.u.SystemTime;

                PrintToConsole("System Time is: %d/%d/%d %d:%d:%d:%d\n", 
                    SystemTimeToUse->wMonth,
                    SystemTimeToUse->wDay,
                    SystemTimeToUse->wYear,
                    SystemTimeToUse->wHour,
                    SystemTimeToUse->wMinute,
                    SystemTimeToUse->wSecond,
                    SystemTimeToUse->wMilliseconds);
                PrintToConsole("Generating component is %d\n", 
                    ErrorInfo.GeneratingComponent);
                PrintToConsole("Status is %d\n", ErrorInfo.Status);
                PrintToConsole("Detection location is %d\n", 
                    (int)ErrorInfo.DetectionLocation);
                PrintToConsole("Flags is %d\n", ErrorInfo.Flags);
                PrintToConsole("NumberOfParameters is %d\n", 
                    ErrorInfo.NumberOfParameters);
                for (i = 0; i < ErrorInfo.NumberOfParameters; i ++)
                    {
                    switch(ErrorInfo.Parameters[i].ParameterType)
                        {
                        case eeptAnsiString:
                            PrintToConsole("Ansi string: %s\n", 
                                ErrorInfo.Parameters[i].u.AnsiString);
                            if (CopyStrings)
                                {
                                Result = HeapFree(GetProcessHeap(), 0, 
                                    ErrorInfo.Parameters[i].u.AnsiString);
                                ASSERT(Result);
                                }
                            break;

                        case eeptUnicodeString:
                            PrintToConsole("Unicode string: %S\n", 
                                ErrorInfo.Parameters[i].u.UnicodeString);
                            if (CopyStrings)
                                {
                                Result = HeapFree(GetProcessHeap(), 0, 
                                    ErrorInfo.Parameters[i].u.UnicodeString);
                                ASSERT(Result);
                                }
                            break;

                        case eeptLongVal:
                            PrintToConsole("Long val: %d\n", 
                                ErrorInfo.Parameters[i].u.LVal);
                            break;

                        case eeptShortVal:
                            PrintToConsole("Short val: %d\n", 
                                (int)ErrorInfo.Parameters[i].u.SVal);
                            break;

                        case eeptPointerVal:
                            PrintToConsole("Pointer val: %d\n", 
                                ErrorInfo.Parameters[i].u.PVal);
                            break;

                        case eeptNone:
                            PrintToConsole("Truncated\n");
                            break;

                        default:
                            PrintToConsole("Invalid type: %d\n", 
                                ErrorInfo.Parameters[i].ParameterType);
                        }
                    }
                }
            }
        RpcErrorEndEnumeration(&EnumHandle);
        }
    }
```



In this example the extended error information is dumped to the console, but your component can make it available to the user in any other way. If your component chooses to save the information in persistent storage and show it later, it is often easier to use the binary format made available by the [**RpcErrorSaveErrorInfo**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcerrorsaveerrorinfo) and [**RpcErrorLoadErrorInfo**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcerrorloaderrorinfo) function calls.

 

 





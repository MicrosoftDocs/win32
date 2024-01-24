---
description: The Win32\_LogicalDiskToPartition association WMI class relates a logical disk drive and the disk partition it resides on.
ms.assetid: 41161d57-d392-4acc-a22a-10be75aa14a6
ms.tgt_platform: multiple
title: Win32_LogicalDiskToPartition class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_LogicalDiskToPartition
- Win32_LogicalDiskToPartition.EndingAddress
- Win32_LogicalDiskToPartition.StartingAddress
- Win32_LogicalDiskToPartition.Antecedent
- Win32_LogicalDiskToPartition.Dependent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_LogicalDiskToPartition class

The **Win32\_LogicalDiskToPartition** association [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) relates a logical disk drive and the disk partition it resides on.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{8502C4FB-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_LogicalDiskToPartition : CIM_LogicalDiskBasedOnPartition
{
  uint64                  EndingAddress;
  uint64                  StartingAddress;
  Win32_DiskPartition REF Antecedent;
  Win32_LogicalDisk   REF Dependent;
};
```

## Members

The **Win32\_LogicalDiskToPartition** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_LogicalDiskToPartition** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_DiskPartition**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("WMI\|Win32\_DiskPartition")
</dt> </dl>

Reference to the instance representing the properties of a disk partition where the logical disk resides.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_LogicalDisk**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("WMI\|Win32\_LogicalDisk")
</dt> </dl>

Reference to the instance representing the properties of a logical disk that resides on a physical disk partition.

</dd> <dt>

**EndingAddress**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the end of the high-level extent in lower-level storage. This property is useful when mapping non-contiguous extents into a higher-level grouping.

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

This property is inherited from [**CIM\_BasedOn**](cim-basedon.md).

</dd> <dt>

**StartingAddress**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the beginning of the high-level extent in lower-level storage.

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

This property is inherited from [**CIM\_BasedOn**](cim-basedon.md).

</dd> </dl>

## Remarks

The **Win32\_LogicalDiskToPartition** class is derived from [**CIM\_LogicalDiskBasedOnPartition**](cim-logicaldiskbasedonpartition.md).

For more information on mapping between a logical drive and a physical disk, see [How Can I Correlate Logical Drives and Physical Disks?](https://devblogs.microsoft.com/scripting/how-can-i-correlate-logical-drives-and-physical-disks/).

## Examples

The following C++ code sample describes how to retrieve the drive letters for a specified disk drive.


```C++
#define _WIN32_DCOM
#include <iostream>
using namespace std;
#include <comdef.h>


#include <Wbemidl.h>

#pragma comment(lib, "wbemuuid.lib")


  
BOOL wmi_run();
BOOL wmi_getDriveLetters();
BOOL wmi_close();


  
IWbemLocator *pLoc = NULL;
IWbemServices *pSvc = NULL;


  
int main(int argc, char **argv)
{
    wmi_run();
    wmi_getDriveLetters();

    system("pause");
    wmi_close();
}


  
//
// Step 1-5 at:
// https://msdn.microsoft.com/library/aa390423(VS.85).aspx
BOOL wmi_run()
{
     HRESULT hres;

    // Step 1: --------------------------------------------------
    // Initialize COM. ------------------------------------------

    hres =  CoInitializeEx(0, COINIT_MULTITHREADED); 
    if (FAILED(hres))
    {
        cout << "Failed to initialize COM library. Error code = 0x" 
            << hex << hres << endl;
        return 1;                  // Program has failed.
    }

    // Step 2: --------------------------------------------------
    // Set general COM security levels --------------------------
    // Note: If you are using Windows 2000, you need to specify -
    // the default authentication credentials for a user by using
    // a SOLE_AUTHENTICATION_LIST structure in the pAuthList ----
    // parameter of CoInitializeSecurity ------------------------

    hres =  CoInitializeSecurity(
        NULL, 
        -1,                          // COM authentication
        NULL,                        // Authentication services
        NULL,                        // Reserved
        RPC_C_AUTHN_LEVEL_DEFAULT,   // Default authentication 
        RPC_C_IMP_LEVEL_IMPERSONATE, // Default Impersonation  
        NULL,                        // Authentication info
        EOAC_NONE,                   // Additional capabilities 
        NULL                         // Reserved
        );


  
    if (FAILED(hres))
    {
        cout << "Failed to initialize security. Error code = 0x" 
            << hex << hres << endl;
        CoUninitialize();
        return 1;                    // Program has failed.
    }

    // Step 3: ---------------------------------------------------
    // Obtain the initial locator to WMI -------------------------

    //IWbemLocator *pLoc = NULL;

    hres = CoCreateInstance(
        CLSID_WbemLocator,             
        0, 
        CLSCTX_INPROC_SERVER, 
        IID_IWbemLocator, (LPVOID *) &pLoc);

    if (FAILED(hres))
    {
        cout << "Failed to create IWbemLocator object."
            << " Err code = 0x"
            << hex << hres << endl;
        CoUninitialize();
        return 1;                 // Program has failed.
    }

    // Step 4: -----------------------------------------------------
    // Connect to WMI through the IWbemLocator::ConnectServer method

    //IWbemServices *pSvc = NULL;

    // Connect to the root\cimv2 namespace with
    // the current user and obtain pointer pSvc
    // to make IWbemServices calls.
    hres = pLoc->ConnectServer(
         _bstr_t(L"ROOT\\CIMV2"), // Object path of WMI namespace
         NULL,                    // User name. NULL = current user
         NULL,                    // User password. NULL = current
         0,                       // Locale. NULL indicates current
         NULL,                    // Security flags.
         0,                       // Authority (e.g. Kerberos)
         0,                       // Context object 
         &pSvc                    // pointer to IWbemServices proxy
         );

    if (FAILED(hres))
    {
        cout << "Could not connect. Error code = 0x" 
             << hex << hres << endl;
        pLoc->Release();     
        CoUninitialize();
        return 1;                // Program has failed.
    }

    cout << "Connected to ROOT\\CIMV2 WMI namespace" << endl;

    // Step 5: --------------------------------------------------
    // Set security levels on the proxy -------------------------

    hres = CoSetProxyBlanket(
       pSvc,                        // Indicates the proxy to set
       RPC_C_AUTHN_WINNT,           // RPC_C_AUTHN_xxx
       RPC_C_AUTHZ_NONE,            // RPC_C_AUTHZ_xxx
       NULL,                        // Server principal name 
       RPC_C_AUTHN_LEVEL_CALL,      // RPC_C_AUTHN_LEVEL_xxx 
       RPC_C_IMP_LEVEL_IMPERSONATE, // RPC_C_IMP_LEVEL_xxx
       NULL,                        // client identity
       EOAC_NONE                    // proxy capabilities 
    );

    if (FAILED(hres))
    {
        cout << "Could not set proxy blanket. Error code = 0x" 
            << hex << hres << endl;
        pSvc->Release();
        pLoc->Release();     
        CoUninitialize();
        return 1;               // Program has failed.
    }
 return 0;
}


  
//
// get Drives, logical Drives and Driveletters
BOOL wmi_getDriveLetters()
{

    // Use the IWbemServices pointer to make requests of WMI. 
    // Make requests here:
    HRESULT hres;
    IEnumWbemClassObject* pEnumerator = NULL;

    // get localdrives
    hres = pSvc->ExecQuery(
                    bstr_t("WQL"), 
                    bstr_t("SELECT * FROM Win32_DiskDrive"),
                    WBEM_FLAG_FORWARD_ONLY | WBEM_FLAG_RETURN_IMMEDIATELY, 
                    NULL,
                    &pEnumerator);

    if (FAILED(hres)) {
        cout << "Query for processes failed. "
             << "Error code = 0x" 
             << hex << hres << endl;
        pSvc->Release();
        pLoc->Release();     
        CoUninitialize();
        return FALSE;               // Program has failed.
    }
    else { 

        IWbemClassObject *pclsObj;
        ULONG uReturn = 0;
        while (pEnumerator) {
           hres = pEnumerator->Next(WBEM_INFINITE, 1, 
                                 &pclsObj, &uReturn);
           if(0 == uReturn) break;

           VARIANT vtProp;
           hres = pclsObj->Get(_bstr_t(L"DeviceID"), 0, &vtProp, 0, 0);

           // adjust string
           wstring tmp = vtProp.bstrVal;
           tmp = tmp.substr(4);

           wstring wstrQuery = L"Associators of {Win32_DiskDrive.DeviceID='\\\\.\\";
           wstrQuery += tmp;
           wstrQuery += L"'} where AssocClass=Win32_DiskDriveToDiskPartition";

           // reference drive to partition
           IEnumWbemClassObject* pEnumerator1 = NULL;
           hres = pSvc->ExecQuery(
                             bstr_t("WQL"), 
                             bstr_t( wstrQuery.c_str()),
                             WBEM_FLAG_FORWARD_ONLY | WBEM_FLAG_RETURN_IMMEDIATELY, 
                             NULL,
                             &pEnumerator1 );

           if ( FAILED(hres) ) {
            cout << "Query for processes failed. "
                          << "Error code = 0x" 
                          << hex << hres << endl;
            pSvc->Release();
            pLoc->Release();     
            CoUninitialize();
            return FALSE;               // Program has failed.
           } else {

                IWbemClassObject *pclsObj1;
                ULONG uReturn1 = 0;
                while( pEnumerator1 ) {
                     hres = pEnumerator1->Next( WBEM_INFINITE, 1, 
                     &pclsObj1, &uReturn1 );
                     if(0 == uReturn1) break;

                     // reference logical drive to partition
                     VARIANT vtProp1;
                     hres = pclsObj1->Get( _bstr_t(L"DeviceID"), 0, &vtProp1, 0, 0 );
                     wstring wstrQuery = L"Associators of {Win32_DiskPartition.DeviceID='";
                     wstrQuery += vtProp1.bstrVal;
                     wstrQuery += L"'} where AssocClass=Win32_LogicalDiskToPartition";


  
                     IEnumWbemClassObject* pEnumerator2 = NULL;
                     hres = pSvc->ExecQuery(
                                       bstr_t("WQL"), 
                                       bstr_t(wstrQuery.c_str()),
                                       WBEM_FLAG_FORWARD_ONLY | WBEM_FLAG_RETURN_IMMEDIATELY, 
                                       NULL,
                                       &pEnumerator2 );





                    if ( FAILED(hres) ) {
                        cout << "Query for processes failed. "
                                << "Error code = 0x" 
                                << hex << hres << endl;
                        pSvc->Release();
                        pLoc->Release();     
                        CoUninitialize();
                        return FALSE;               // Program has failed.
                     } else {

                        // get driveletter
                        IWbemClassObject *pclsObj2;
                        ULONG uReturn2 = 0;
                        while( pEnumerator2 ) {
                            hres = pEnumerator2->Next( WBEM_INFINITE, 1, 
                            &pclsObj2, &uReturn2 );
                            if(0 == uReturn2) break;

                            VARIANT vtProp2;
                            hres = pclsObj2->Get( _bstr_t(L"DeviceID"), 0, &vtProp2, 0, 0 );


  
                            // print result
                            printf("%ls : %ls\n", vtProp.bstrVal, vtProp2.bstrVal);

                            VariantClear( &vtProp2 );
                        }
                        pclsObj1->Release();
                    }
                    VariantClear( &vtProp1 );
                    pEnumerator2->Release();
                }
                pclsObj->Release();
            }
            VariantClear( &vtProp );
            pEnumerator1->Release();
        }
     }
     pEnumerator->Release();
     return TRUE;
}






BOOL wmi_close()
{
 // Cleanup
    // ========

    pSvc->Release();
    pLoc->Release();
    CoUninitialize();

    return 0;   // Program successfully completed. 
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_LogicalDiskBasedOnPartition**](cim-logicaldiskbasedonpartition.md)
</dt> <dt>

[Operating System Classes](/previous-versions//aa392727(v=vs.85))
</dt> <dt>

[WMI Tasks: Disks and File Systems](/windows/desktop/WmiSdk/wmi-tasks--disks-and-file-systems)
</dt> </dl>


---
title: Passing a Safearray of UDTs
description: For passing a safearrray of UDTs, the designer of the server describes the data types of the UDT in a IDL file. The client needs the type library to fetch the IRecordInfo Interface. The safearray is then created with SafeArrayCreateEx.
ms.assetid: 55a1effb-067f-4ae7-9e88-bccbfd7da433
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Passing a Safearray of UDTs

For passing a safearrray of UDTs, the designer of the server describes the data types of the UDT in a IDL file. The client needs the type library to fetch the [**IRecordInfo**](/windows/previous-versions/oaidl/nn-oaidl-irecordinfo?branch=master) Interface. The safearray is then created with [**SafeArrayCreateEx**](/windows/previous-versions/OleAuto/nf-oleauto-safearraycreateex?branch=master).

The following is the IDL for a safearray of UDTs to be passed:


```C++
library Student
{
importlib("stdole2.tlb");
typedef enum tagclassification {school_Bully, class_Clown, teachers_Favorite} classification;
typedef [uuid(D8B3861A-74C6-11d2-A0D6-00C04FB17CDB)] struct tagStudentStruct {
      BSTR name;
      short grade;
      classification  type;
      VARIANT_BOOL   graduate;
} StudentStruct;
[
object,
uuid(D50BD660-7471-11d2-9A80-006097DA88F5),         // IID_IStudent
helpstring("User Defined Data Server"),
dual,
pointer_default(unique)
]
interface IStudent : IDispatch
{
import "unknwn.idl";
typedef IStudent* LPSTUDENT;

HRESULT Test2([in,out] SAFEARRAY(StudentStruct));
};
```



For passing a safearray of UDTs the type library is necessary for fetching the [**IRecordInfo**](/windows/previous-versions/oaidl/nn-oaidl-irecordinfo?branch=master) Interface. The type library of the UDT is first loaded by calling [**LoadRegTypeLib**](/windows/previous-versions/OleAuto/nf-oleauto-loadregtypelib?branch=master) and the type information of the UDT is obtained with [**GetTypeInfoOfGuid**](/windows/previous-versions/oaidl/nf-oaidl-itypelib-gettypeinfoofguid?branch=master). The [**GetRecordInfoFromTypeInfo**](/windows/previous-versions/OleAuto/nf-oleauto-getrecordinfofromtypeinfo?branch=master) function is then called to obtain the record information from the type information of the UDT. At this point the record information is returned to *pRecInfo*.


```C++
LPTYPEINF pTypeInfo = NULL;
LPTYPELIB pTypelib = NULL;
LPSAFEARRAY psaStudent = NULL;
SAFEARRAYBOUND rgbounds = { 4, 0 };
StudentStruct *pStudentStruct = NULL;
IRecordInfo* pRecInfo = NULL;

// Fetch the IRecordInfo interface describing the UDT
hr = LoadRegTypeLib(LIBID_Student, 1, 0, GetUserDefaultLCID(), &amp;pTypelib);
_ASSERT(SUCCEEDED(hr) &amp;&amp; pTypelib);

hr = pTypelib->GetTypeInfoOfGuid(UUID_StudentStruct, &amp;pTypeInfo);
_ASSERT(SUCCEEDED(hr) &amp;&amp; pTypeInfo);
hr = GetRecordInfoFromTypeInfo(pTypeInfo, &amp;pRecInfo);
_ASSERT(SUCCEEDED(hr) &amp;&amp; pRecInfo);
RELEASEINTERFACE(pTypeInfo);
RELEASEINTERFACE(pTypelib);
```



After *pRecInfo* is obtained from the type library, [**SafeArrayCreateEx**](/windows/previous-versions/OleAuto/nf-oleauto-safearraycreateex?branch=master) is called to create the safearray, where its last parameter is *pRecInfo*. [**SafeArrayAccessData**](/windows/previous-versions/OleAuto/nf-oleauto-safearrayaccessdata?branch=master) is then called to increment the lock count of the array.


```C++
psaStudent = SafeArrayCreateEx(VT_RECORD, 1, &amp;rgbounds, pRecInfo);
RELEASEINTERFACE(pRecInfo);
_ASSERT(psaStudent);
hr = SafeArrayAccessData(psaStudent, reinterpret_cast<PVOID*>(&amp;pStudentStruct));
_ASSERT(SUCCEEDED(hr) &amp;&amp; pStudentStruct);
```



Then the StudentStruct safearray of UDTs is declared and assigned some values:


```C++
pStudentStruct[0].grade = 3;
pStudentStruct[0].name = SysAllocString(L"Shaun");
pStudentStruct[0].type = class_Clown;
pStudentStruct[1].grade = 8;
pStudentStruct[1].name = SysAllocString(L"Fred");
pStudentStruct[1].type = school_Bully;
pStudentStruct[2].grade = 12;
pStudentStruct[2].name = SysAllocString(L"Steve");
pStudentStruct[2].type = teachers_Favorite;
pStudentStruct[3].grade = 3;
pStudentStruct[3].name = SysAllocString(L"Linda");
pStudentStruct[3].type = teachers_Favorite;
```



[**SafeArrayUnaccessData**](/windows/previous-versions/OleAuto/nf-oleauto-safearrayunaccessdata?branch=master) is then called to decrement the lock count of the array, and invalidate the pointer retrieved by [**SafeArrayAccessData**](/windows/previous-versions/OleAuto/nf-oleauto-safearrayaccessdata?branch=master):


```C++
hr = SafeArrayUnaccessData(psaStudent);
_ASSERT(SUCCEEDED(hr));
```



The safearray is then passed to the Test2 method:


```C++
hr = pStudent->Test2(psaStudent);
```



## Related topics

<dl> <dt>

[**SafeArrayGetRecordInfo**](/windows/previous-versions/OleAuto/nf-oleauto-safearraygetrecordinfo?branch=master)
</dt> <dt>

[**SafeArraySetRecordInfo**](/windows/previous-versions/OleAuto/nf-oleauto-safearraysetrecordinfo?branch=master)
</dt> <dt>

[**SafeArrayAllocDescriptorEx**](/windows/previous-versions/OleAuto/nf-oleauto-safearrayallocdescriptorex?branch=master)
</dt> <dt>

[**ITypeLib::GetTypeInfoOfGuid**](/windows/previous-versions/oaidl/nf-oaidl-itypelib-gettypeinfoofguid?branch=master)
</dt> <dt>

[**SafeArrayCreateEx**](/windows/previous-versions/OleAuto/nf-oleauto-safearraycreateex?branch=master)
</dt> <dt>

[**SafeArrayCreateVectorEx**](/windows/previous-versions/OleAuto/nf-oleauto-safearraycreatevectorex?branch=master)
</dt> <dt>

[**SafeArrayUnaccessData**](/windows/previous-versions/OleAuto/nf-oleauto-safearrayunaccessdata?branch=master)
</dt> <dt>

[**SafeArrayAccessData**](/windows/previous-versions/OleAuto/nf-oleauto-safearrayaccessdata?branch=master)
</dt> </dl>

 

 





---
title: Array Manipulation Functions
description: The arrays passed by IDispatch Invoke within VARIANTARG are called safearrays.
ms.assetid: 28a00e34-3b5e-4a16-9f4c-dd2a72dc8e46
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Array Manipulation Functions

The arrays passed by [**IDispatch::Invoke**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-idispatch-invoke) within **VARIANTARG** are called safearrays. A safearray contains information about the number of dimensions and bounds within them. When an array is an argument or the return value of a function, the **parray** field of **VARIANTARG** points to an array descriptor. Do not access this array descriptor directly, unless you are creating arrays containing elements with nonvariant data types. Instead, use the functions [**SafeArrayAccessData**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearrayaccessdata) and [**SafeArrayUnaccessData**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearrayunaccessdata) to access the data.

The base type of the array is indicated by VT\_ tag \| VT\_ARRAY. The data referenced by an array descriptor is stored in column-major order, which is the same ordering scheme used by Visual Basic and FORTRAN, but different from C and Pascal. Column-major order is when the left-most dimension (as specified in a programming language syntax) changes first.

The following table contains the functions you use when accessing the data in the descriptor and the array.

## In this section



| Topic                                                                       | Description                                                                                                                                                                                                                                                                                     |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SafeArrayAccessData**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearrayaccessdata)<br/>               | Increments the lock count of an array, and retrieves a pointer to the array data.<br/>                                                                                                                                                                                                    |
| [**SafeArrayAddRef**](/previous-versions/windows/desktop/api/Oleauto/nf-oleauto-safearrayaddref)<br/>                       | Increases the pinning reference count of the descriptor for the specified safe array by one, and may increase the pinning reference count of the data for the specified safe array by one if that data was dynamically allocated, as determined by the descriptor of the safe array.<br/> |
| [**SafeArrayAllocData**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearrayallocdata)<br/>                 | Allocates memory for a safe array, based on a descriptor created with [**SafeArrayAllocDescriptor**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearrayallocdescriptor).<br/>                                                                                                                                                  |
| [**SafeArrayAllocDescriptor**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearrayallocdescriptor)<br/>     | Allocates memory for a safe array descriptor.<br/>                                                                                                                                                                                                                                        |
| [**SafeArrayAllocDescriptorEx**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearrayallocdescriptorex)<br/> | Creates a safe array descriptor for an array of any valid variant type, including VT\_RECORD, without allocating the array data.<br/>                                                                                                                                                     |
| [**SafeArrayCopy**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearraycopy)<br/>                           | Creates a copy of an existing safe array.<br/>                                                                                                                                                                                                                                            |
| [**SafeArrayCopyData**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearraycopydata)<br/>                   | Copies the source array to the specified target array after releasing any resources in the target array.<br/>                                                                                                                                                                             |
| [**SafeArrayCreate**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearraycreate)<br/>                       | Creates a new array descriptor, allocates and initializes the data for the array, and returns a pointer to the new array descriptor.<br/>                                                                                                                                                 |
| [**SafeArrayCreateEx**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearraycreateex)<br/>                   | Creates and returns a safe array descriptor from the specified VARTYPE, number of dimensions and bounds.<br/>                                                                                                                                                                             |
| [**SafeArrayCreateVector**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearraycreatevector)<br/>           | Creates a one-dimensional array. A safe array created with [**SafeArrayCreateVector**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearraycreatevector) is a fixed size, so the constant FADF\_FIXEDSIZE is always set.<br/>                                                                                                    |
| [**SafeArrayCreateVectorEx**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearraycreatevectorex)<br/>       | Creates and returns a one-dimensional safe array of the specified VARTYPE and bounds.<br/>                                                                                                                                                                                                |
| [**SafeArrayDestroy**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearraydestroy)<br/>                     | Destroys an existing array descriptor and all of the data in the array.<br/>                                                                                                                                                                                                              |
| [**SafeArrayDestroyData**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearraydestroydata)<br/>             | Destroys all the data in the specified safe array. <br/>                                                                                                                                                                                                                                  |
| [**SafeArrayDestroyDescriptor**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearraydestroydescriptor)<br/> | Destroys the descriptor of the specified safe array.<br/>                                                                                                                                                                                                                                 |
| [**SafeArrayGetDim**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearraygetdim)<br/>                       | Gets the number of dimensions in the array.<br/>                                                                                                                                                                                                                                          |
| [**SafeArrayGetElement**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearraygetelement)<br/>               | Retrieves a single element of the array.<br/>                                                                                                                                                                                                                                             |
| [**SafeArrayGetElemsize**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearraygetelemsize)<br/>             | Gets the size of an element.<br/>                                                                                                                                                                                                                                                         |
| [**SafeArrayGetIID**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearraygetiid)<br/>                       | Gets the GUID of the interface contained within the specified safe array.<br/>                                                                                                                                                                                                            |
| [**SafeArrayGetLBound**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearraygetlbound)<br/>                 | Gets the lower bound for any dimension of the specified safe array.<br/>                                                                                                                                                                                                                  |
| [**SafeArrayGetRecordInfo**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearraygetrecordinfo)<br/>         | Retrieves the [**IRecordInfo**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-irecordinfo) interface of the UDT contained in the specified safe array.<br/>                                                                                                                                                                         |
| [**SafeArrayGetUBound**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearraygetubound)<br/>                 | Gets the upper bound for any dimension of the specified safe array.<br/>                                                                                                                                                                                                                  |
| [**SafeArrayGetVartype**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearraygetvartype)<br/>               | Gets the VARTYPE stored in the specified safe array.<br/>                                                                                                                                                                                                                                 |
| [**SafeArrayLock**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearraylock)<br/>                           | Increments the lock count of an array, and places a pointer to the array data in pvData of the array descriptor.<br/>                                                                                                                                                                     |
| [**SafeArrayPtrOfIndex**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearrayptrofindex)<br/>               | Gets a pointer to an array element.<br/>                                                                                                                                                                                                                                                  |
| [**SafeArrayPutElement**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearrayputelement)<br/>               | Stores the data element at the specified location in the array.<br/>                                                                                                                                                                                                                      |
| [**SafeArrayRedim**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearrayredim)<br/>                         | Changes the right-most (least significant) bound of the specified safe array.<br/>                                                                                                                                                                                                        |
| [**SafeArrayReleaseData**](/previous-versions/windows/desktop/api/Oleauto/nf-oleauto-safearrayreleasedata)<br/>             | Decreases the pinning reference count for the specified safe array data by one. When that count reaches 0, the memory for that data is no longer prevented from being freed.<br/>                                                                                                         |
| [**SafeArrayReleaseDescriptor**](/previous-versions/windows/desktop/api/Oleauto/nf-oleauto-safearrayreleasedescriptor)<br/> | Decreases the pinning reference count for the descriptor of the specified safe array by one. When that count reaches 0, the memory for that descriptor is no longer prevented from being freed.<br/>                                                                                      |
| [**SafeArraySetIID**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearraysetiid)<br/>                       | Sets the GUID of the interface for the specified safe array. <br/>                                                                                                                                                                                                                        |
| [**SafeArraySetRecordInfo**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearraysetrecordinfo)<br/>         | Sets the record info in the specified safe array.<br/>                                                                                                                                                                                                                                    |
| [**SafeArrayUnaccessData**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearrayunaccessdata)<br/>           | Decrements the lock count of an array, and invalidates the pointer retrieved by [**SafeArrayAccessData**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearrayaccessdata).<br/>                                                                                                                                                  |
| [**SafeArrayUnlock**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-safearrayunlock)<br/>                       | Decrements the lock count of an array so it can be freed or resized.<br/>                                                                                                                                                                                                                 |
| [**SAFEARRAY**](/previous-versions/windows/desktop/api/OaIdl/ns-oaidl-tagsafearray)<br/>                                   | Represents a safe array.<br/>                                                                                                                                                                                                                                                             |
| [**SAFEARRAYBOUND**](/previous-versions/windows/desktop/api/OaIdl/ns-oaidl-tagsafearraybound)<br/>                         | Represents the bounds of one dimension of the array.<br/>                                                                                                                                                                                                                                 |



 

## Related topics

<dl> <dt>

[Conversion and Manipulation Functions](conversion-and-manipulation-functions.md)
</dt> <dt>

[**SAFEARRAY Data Type**](/previous-versions/windows/desktop/api/OaIdl/ns-oaidl-tagsafearray)
</dt> <dt>

[**SAFEARRAYBOUND Structure**](/previous-versions/windows/desktop/api/OaIdl/ns-oaidl-tagsafearraybound)
</dt> </dl>

 

 






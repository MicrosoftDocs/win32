---
title: Array Manipulation Functions
description: The arrays passed by IDispatch Invoke within VARIANTARG are called safearrays.
ms.assetid: 28a00e34-3b5e-4a16-9f4c-dd2a72dc8e46
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Array Manipulation Functions

The arrays passed by [**IDispatch::Invoke**](/windows/previous-versions/oaidl/nf-oaidl-idispatch-invoke?branch=master) within **VARIANTARG** are called safearrays. A safearray contains information about the number of dimensions and bounds within them. When an array is an argument or the return value of a function, the **parray** field of **VARIANTARG** points to an array descriptor. Do not access this array descriptor directly, unless you are creating arrays containing elements with nonvariant data types. Instead, use the functions [**SafeArrayAccessData**](/windows/previous-versions/OleAuto/nf-oleauto-safearrayaccessdata?branch=master) and [**SafeArrayUnaccessData**](/windows/previous-versions/OleAuto/nf-oleauto-safearrayunaccessdata?branch=master) to access the data.

The base type of the array is indicated by VT\_ tag \| VT\_ARRAY. The data referenced by an array descriptor is stored in column-major order, which is the same ordering scheme used by Visual Basic and FORTRAN, but different from C and Pascal. Column-major order is when the left-most dimension (as specified in a programming language syntax) changes first.

The following table contains the functions you use when accessing the data in the descriptor and the array.

## In this section



| Topic                                                                       | Description                                                                                                                                                                                                                                                                                     |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SafeArrayAccessData**](/windows/previous-versions/OleAuto/nf-oleauto-safearrayaccessdata?branch=master)<br/>               | Increments the lock count of an array, and retrieves a pointer to the array data.<br/>                                                                                                                                                                                                    |
| [**SafeArrayAddRef**](/windows/previous-versions/Oleauto/nf-oleauto-safearrayaddref?branch=master)<br/>                       | Increases the pinning reference count of the descriptor for the specified safe array by one, and may increase the pinning reference count of the data for the specified safe array by one if that data was dynamically allocated, as determined by the descriptor of the safe array.<br/> |
| [**SafeArrayAllocData**](/windows/previous-versions/OleAuto/nf-oleauto-safearrayallocdata?branch=master)<br/>                 | Allocates memory for a safe array, based on a descriptor created with [**SafeArrayAllocDescriptor**](/windows/previous-versions/OleAuto/nf-oleauto-safearrayallocdescriptor?branch=master).<br/>                                                                                                                                                  |
| [**SafeArrayAllocDescriptor**](/windows/previous-versions/OleAuto/nf-oleauto-safearrayallocdescriptor?branch=master)<br/>     | Allocates memory for a safe array descriptor.<br/>                                                                                                                                                                                                                                        |
| [**SafeArrayAllocDescriptorEx**](/windows/previous-versions/OleAuto/nf-oleauto-safearrayallocdescriptorex?branch=master)<br/> | Creates a safe array descriptor for an array of any valid variant type, including VT\_RECORD, without allocating the array data.<br/>                                                                                                                                                     |
| [**SafeArrayCopy**](/windows/previous-versions/OleAuto/nf-oleauto-safearraycopy?branch=master)<br/>                           | Creates a copy of an existing safe array.<br/>                                                                                                                                                                                                                                            |
| [**SafeArrayCopyData**](/windows/previous-versions/OleAuto/nf-oleauto-safearraycopydata?branch=master)<br/>                   | Copies the source array to the specified target array after releasing any resources in the target array.<br/>                                                                                                                                                                             |
| [**SafeArrayCreate**](/windows/previous-versions/OleAuto/nf-oleauto-safearraycreate?branch=master)<br/>                       | Creates a new array descriptor, allocates and initializes the data for the array, and returns a pointer to the new array descriptor.<br/>                                                                                                                                                 |
| [**SafeArrayCreateEx**](/windows/previous-versions/OleAuto/nf-oleauto-safearraycreateex?branch=master)<br/>                   | Creates and returns a safe array descriptor from the specified VARTYPE, number of dimensions and bounds.<br/>                                                                                                                                                                             |
| [**SafeArrayCreateVector**](/windows/previous-versions/OleAuto/nf-oleauto-safearraycreatevector?branch=master)<br/>           | Creates a one-dimensional array. A safe array created with [**SafeArrayCreateVector**](/windows/previous-versions/OleAuto/nf-oleauto-safearraycreatevector?branch=master) is a fixed size, so the constant FADF\_FIXEDSIZE is always set.<br/>                                                                                                    |
| [**SafeArrayCreateVectorEx**](/windows/previous-versions/OleAuto/nf-oleauto-safearraycreatevectorex?branch=master)<br/>       | Creates and returns a one-dimensional safe array of the specified VARTYPE and bounds.<br/>                                                                                                                                                                                                |
| [**SafeArrayDestroy**](/windows/previous-versions/OleAuto/nf-oleauto-safearraydestroy?branch=master)<br/>                     | Destroys an existing array descriptor and all of the data in the array.<br/>                                                                                                                                                                                                              |
| [**SafeArrayDestroyData**](/windows/previous-versions/OleAuto/nf-oleauto-safearraydestroydata?branch=master)<br/>             | Destroys all the data in the specified safe array. <br/>                                                                                                                                                                                                                                  |
| [**SafeArrayDestroyDescriptor**](/windows/previous-versions/OleAuto/nf-oleauto-safearraydestroydescriptor?branch=master)<br/> | Destroys the descriptor of the specified safe array.<br/>                                                                                                                                                                                                                                 |
| [**SafeArrayGetDim**](/windows/previous-versions/OleAuto/nf-oleauto-safearraygetdim?branch=master)<br/>                       | Gets the number of dimensions in the array.<br/>                                                                                                                                                                                                                                          |
| [**SafeArrayGetElement**](/windows/previous-versions/OleAuto/nf-oleauto-safearraygetelement?branch=master)<br/>               | Retrieves a single element of the array.<br/>                                                                                                                                                                                                                                             |
| [**SafeArrayGetElemsize**](/windows/previous-versions/OleAuto/nf-oleauto-safearraygetelemsize?branch=master)<br/>             | Gets the size of an element.<br/>                                                                                                                                                                                                                                                         |
| [**SafeArrayGetIID**](/windows/previous-versions/OleAuto/nf-oleauto-safearraygetiid?branch=master)<br/>                       | Gets the GUID of the interface contained within the specified safe array.<br/>                                                                                                                                                                                                            |
| [**SafeArrayGetLBound**](/windows/previous-versions/OleAuto/nf-oleauto-safearraygetlbound?branch=master)<br/>                 | Gets the lower bound for any dimension of the specified safe array.<br/>                                                                                                                                                                                                                  |
| [**SafeArrayGetRecordInfo**](/windows/previous-versions/OleAuto/nf-oleauto-safearraygetrecordinfo?branch=master)<br/>         | Retrieves the [**IRecordInfo**](/windows/previous-versions/oaidl/nn-oaidl-irecordinfo?branch=master) interface of the UDT contained in the specified safe array.<br/>                                                                                                                                                                         |
| [**SafeArrayGetUBound**](/windows/previous-versions/OleAuto/nf-oleauto-safearraygetubound?branch=master)<br/>                 | Gets the upper bound for any dimension of the specified safe array.<br/>                                                                                                                                                                                                                  |
| [**SafeArrayGetVartype**](/windows/previous-versions/OleAuto/nf-oleauto-safearraygetvartype?branch=master)<br/>               | Gets the VARTYPE stored in the specified safe array.<br/>                                                                                                                                                                                                                                 |
| [**SafeArrayLock**](/windows/previous-versions/OleAuto/nf-oleauto-safearraylock?branch=master)<br/>                           | Increments the lock count of an array, and places a pointer to the array data in pvData of the array descriptor.<br/>                                                                                                                                                                     |
| [**SafeArrayPtrOfIndex**](/windows/previous-versions/OleAuto/nf-oleauto-safearrayptrofindex?branch=master)<br/>               | Gets a pointer to an array element.<br/>                                                                                                                                                                                                                                                  |
| [**SafeArrayPutElement**](/windows/previous-versions/OleAuto/nf-oleauto-safearrayputelement?branch=master)<br/>               | Stores the data element at the specified location in the array.<br/>                                                                                                                                                                                                                      |
| [**SafeArrayRedim**](/windows/previous-versions/OleAuto/nf-oleauto-safearrayredim?branch=master)<br/>                         | Changes the right-most (least significant) bound of the specified safe array.<br/>                                                                                                                                                                                                        |
| [**SafeArrayReleaseData**](/windows/previous-versions/Oleauto/nf-oleauto-safearrayreleasedata?branch=master)<br/>             | Decreases the pinning reference count for the specified safe array data by one. When that count reaches 0, the memory for that data is no longer prevented from being freed.<br/>                                                                                                         |
| [**SafeArrayReleaseDescriptor**](/windows/previous-versions/Oleauto/nf-oleauto-safearrayreleasedescriptor?branch=master)<br/> | Decreases the pinning reference count for the descriptor of the specified safe array by one. When that count reaches 0, the memory for that descriptor is no longer prevented from being freed.<br/>                                                                                      |
| [**SafeArraySetIID**](/windows/previous-versions/OleAuto/nf-oleauto-safearraysetiid?branch=master)<br/>                       | Sets the GUID of the interface for the specified safe array. <br/>                                                                                                                                                                                                                        |
| [**SafeArraySetRecordInfo**](/windows/previous-versions/OleAuto/nf-oleauto-safearraysetrecordinfo?branch=master)<br/>         | Sets the record info in the specified safe array.<br/>                                                                                                                                                                                                                                    |
| [**SafeArrayUnaccessData**](/windows/previous-versions/OleAuto/nf-oleauto-safearrayunaccessdata?branch=master)<br/>           | Decrements the lock count of an array, and invalidates the pointer retrieved by [**SafeArrayAccessData**](/windows/previous-versions/OleAuto/nf-oleauto-safearrayaccessdata?branch=master).<br/>                                                                                                                                                  |
| [**SafeArrayUnlock**](/windows/previous-versions/OleAuto/nf-oleauto-safearrayunlock?branch=master)<br/>                       | Decrements the lock count of an array so it can be freed or resized.<br/>                                                                                                                                                                                                                 |
| [**SAFEARRAY**](/windows/previous-versions/OaIdl/ns-oaidl-tagsafearray?branch=master)<br/>                                   | Represents a safe array.<br/>                                                                                                                                                                                                                                                             |
| [**SAFEARRAYBOUND**](/windows/previous-versions/OaIdl/ns-oaidl-tagsafearraybound?branch=master)<br/>                         | Represents the bounds of one dimension of the array.<br/>                                                                                                                                                                                                                                 |



 

## Related topics

<dl> <dt>

[Conversion and Manipulation Functions](conversion-and-manipulation-functions.md)
</dt> <dt>

[**SAFEARRAY Data Type**](/windows/previous-versions/OaIdl/ns-oaidl-tagsafearray?branch=master)
</dt> <dt>

[**SAFEARRAYBOUND Structure**](/windows/previous-versions/OaIdl/ns-oaidl-tagsafearraybound?branch=master)
</dt> </dl>

 

 






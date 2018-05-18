---
title: Array Manipulation Functions
description: The arrays passed by IDispatch Invoke within VARIANTARG are called safearrays.
ms.assetid: '28a00e34-3b5e-4a16-9f4c-dd2a72dc8e46'
---

# Array Manipulation Functions

The arrays passed by [**IDispatch::Invoke**](idispatch-invoke.md) within **VARIANTARG** are called safearrays. A safearray contains information about the number of dimensions and bounds within them. When an array is an argument or the return value of a function, the **parray** field of **VARIANTARG** points to an array descriptor. Do not access this array descriptor directly, unless you are creating arrays containing elements with nonvariant data types. Instead, use the functions [**SafeArrayAccessData**](safearrayaccessdata.md) and [**SafeArrayUnaccessData**](safearrayunaccessdata.md) to access the data.

The base type of the array is indicated by VT\_ tag \| VT\_ARRAY. The data referenced by an array descriptor is stored in column-major order, which is the same ordering scheme used by Visual Basic and FORTRAN, but different from C and Pascal. Column-major order is when the left-most dimension (as specified in a programming language syntax) changes first.

The following table contains the functions you use when accessing the data in the descriptor and the array.

## In this section



| Topic                                                                       | Description                                                                                                                                                                                                                                                                                     |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SafeArrayAccessData**](safearrayaccessdata.md)<br/>               | Increments the lock count of an array, and retrieves a pointer to the array data.<br/>                                                                                                                                                                                                    |
| [**SafeArrayAddRef**](safearrayaddref.md)<br/>                       | Increases the pinning reference count of the descriptor for the specified safe array by one, and may increase the pinning reference count of the data for the specified safe array by one if that data was dynamically allocated, as determined by the descriptor of the safe array.<br/> |
| [**SafeArrayAllocData**](safearrayallocdata.md)<br/>                 | Allocates memory for a safe array, based on a descriptor created with [**SafeArrayAllocDescriptor**](safearrayallocdescriptor.md).<br/>                                                                                                                                                  |
| [**SafeArrayAllocDescriptor**](safearrayallocdescriptor.md)<br/>     | Allocates memory for a safe array descriptor.<br/>                                                                                                                                                                                                                                        |
| [**SafeArrayAllocDescriptorEx**](safearrayallocdescriptorex.md)<br/> | Creates a safe array descriptor for an array of any valid variant type, including VT\_RECORD, without allocating the array data.<br/>                                                                                                                                                     |
| [**SafeArrayCopy**](safearraycopy.md)<br/>                           | Creates a copy of an existing safe array.<br/>                                                                                                                                                                                                                                            |
| [**SafeArrayCopyData**](safearraycopydata.md)<br/>                   | Copies the source array to the specified target array after releasing any resources in the target array.<br/>                                                                                                                                                                             |
| [**SafeArrayCreate**](safearraycreate.md)<br/>                       | Creates a new array descriptor, allocates and initializes the data for the array, and returns a pointer to the new array descriptor.<br/>                                                                                                                                                 |
| [**SafeArrayCreateEx**](safearraycreateex.md)<br/>                   | Creates and returns a safe array descriptor from the specified VARTYPE, number of dimensions and bounds.<br/>                                                                                                                                                                             |
| [**SafeArrayCreateVector**](safearraycreatevector.md)<br/>           | Creates a one-dimensional array. A safe array created with [**SafeArrayCreateVector**](safearraycreatevector.md) is a fixed size, so the constant FADF\_FIXEDSIZE is always set.<br/>                                                                                                    |
| [**SafeArrayCreateVectorEx**](safearraycreatevectorex.md)<br/>       | Creates and returns a one-dimensional safe array of the specified VARTYPE and bounds.<br/>                                                                                                                                                                                                |
| [**SafeArrayDestroy**](safearraydestroy.md)<br/>                     | Destroys an existing array descriptor and all of the data in the array.<br/>                                                                                                                                                                                                              |
| [**SafeArrayDestroyData**](safearraydestroydata.md)<br/>             | Destroys all the data in the specified safe array. <br/>                                                                                                                                                                                                                                  |
| [**SafeArrayDestroyDescriptor**](safearraydestroydescriptor.md)<br/> | Destroys the descriptor of the specified safe array.<br/>                                                                                                                                                                                                                                 |
| [**SafeArrayGetDim**](safearraygetdim.md)<br/>                       | Gets the number of dimensions in the array.<br/>                                                                                                                                                                                                                                          |
| [**SafeArrayGetElement**](safearraygetelement.md)<br/>               | Retrieves a single element of the array.<br/>                                                                                                                                                                                                                                             |
| [**SafeArrayGetElemsize**](safearraygetelemsize.md)<br/>             | Gets the size of an element.<br/>                                                                                                                                                                                                                                                         |
| [**SafeArrayGetIID**](safearraygetiid.md)<br/>                       | Gets the GUID of the interface contained within the specified safe array.<br/>                                                                                                                                                                                                            |
| [**SafeArrayGetLBound**](safearraygetlbound.md)<br/>                 | Gets the lower bound for any dimension of the specified safe array.<br/>                                                                                                                                                                                                                  |
| [**SafeArrayGetRecordInfo**](safearraygetrecordinfo.md)<br/>         | Retrieves the [**IRecordInfo**](irecordinfo.md) interface of the UDT contained in the specified safe array.<br/>                                                                                                                                                                         |
| [**SafeArrayGetUBound**](safearraygetubound.md)<br/>                 | Gets the upper bound for any dimension of the specified safe array.<br/>                                                                                                                                                                                                                  |
| [**SafeArrayGetVartype**](safearraygetvartype.md)<br/>               | Gets the VARTYPE stored in the specified safe array.<br/>                                                                                                                                                                                                                                 |
| [**SafeArrayLock**](safearraylock.md)<br/>                           | Increments the lock count of an array, and places a pointer to the array data in pvData of the array descriptor.<br/>                                                                                                                                                                     |
| [**SafeArrayPtrOfIndex**](safearrayptrofindex.md)<br/>               | Gets a pointer to an array element.<br/>                                                                                                                                                                                                                                                  |
| [**SafeArrayPutElement**](safearrayputelement.md)<br/>               | Stores the data element at the specified location in the array.<br/>                                                                                                                                                                                                                      |
| [**SafeArrayRedim**](safearrayredim.md)<br/>                         | Changes the right-most (least significant) bound of the specified safe array.<br/>                                                                                                                                                                                                        |
| [**SafeArrayReleaseData**](safearrayreleasedata.md)<br/>             | Decreases the pinning reference count for the specified safe array data by one. When that count reaches 0, the memory for that data is no longer prevented from being freed.<br/>                                                                                                         |
| [**SafeArrayReleaseDescriptor**](safearrayreleasedescriptor.md)<br/> | Decreases the pinning reference count for the descriptor of the specified safe array by one. When that count reaches 0, the memory for that descriptor is no longer prevented from being freed.<br/>                                                                                      |
| [**SafeArraySetIID**](safearraysetiid.md)<br/>                       | Sets the GUID of the interface for the specified safe array. <br/>                                                                                                                                                                                                                        |
| [**SafeArraySetRecordInfo**](safearraysetrecordinfo.md)<br/>         | Sets the record info in the specified safe array.<br/>                                                                                                                                                                                                                                    |
| [**SafeArrayUnaccessData**](safearrayunaccessdata.md)<br/>           | Decrements the lock count of an array, and invalidates the pointer retrieved by [**SafeArrayAccessData**](safearrayaccessdata.md).<br/>                                                                                                                                                  |
| [**SafeArrayUnlock**](safearrayunlock.md)<br/>                       | Decrements the lock count of an array so it can be freed or resized.<br/>                                                                                                                                                                                                                 |
| [**SAFEARRAY**](safearray.md)<br/>                                   | Represents a safe array.<br/>                                                                                                                                                                                                                                                             |
| [**SAFEARRAYBOUND**](safearraybound.md)<br/>                         | Represents the bounds of one dimension of the array.<br/>                                                                                                                                                                                                                                 |



 

## Related topics

<dl> <dt>

[Conversion and Manipulation Functions](conversion-and-manipulation-functions.md)
</dt> <dt>

[**SAFEARRAY Data Type**](safearray.md)
</dt> <dt>

[**SAFEARRAYBOUND Structure**](safearraybound.md)
</dt> </dl>

 

 






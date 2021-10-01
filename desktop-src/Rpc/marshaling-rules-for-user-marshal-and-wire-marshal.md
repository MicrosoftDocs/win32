---
title: Marshaling Rules for user_marshal and wire_marshal
description: The OSF-DCE specification for marshaling embedded pointer types requires that you observe the following restrictions when implementing the type \_UserSize, type \_UserMarshal, and type \_UserUnMarshal functions.
ms.assetid: 077cdd1a-9630-459e-8749-ab0c70b16ecb
ms.topic: article
ms.date: 05/31/2018
---

# Marshaling Rules for user\_marshal and wire\_marshal

The OSF-DCE specification for marshaling embedded pointer types requires that you observe the following restrictions when implementing the &lt;type&gt;\_UserSize, &lt;type&gt;\_UserMarshal, and &lt;type&gt;\_UserUnMarshal functions. (The rules and examples given here are for marshaling. However, your sizing and unmarshaling routines must follow the same restrictions):

-   If the wire-type is a flat type with no pointers, your marshaling routine for the corresponding userm-type should simply marshal the data according to the layout of the wire-type. For example:

    ``` syntax
    typedef [wire_marshal (long)] void * HANDLE_HANDLE;
    ```

    Note that the wire type, **long**, is a flat type. Your HANDLE\_HANDLE\_UserMarshal function marshals a **long** whenever a HANDLE\_HANDLE object is passed to it.

-   If the wire-type is a pointer to another type, your marshaling routine for the corresponding userm-type should marshal the data according to the layout for the type that the wire-type points to. The NDR engine takes care of the pointer. For example:

    ``` syntax
    typedef struct HDATA
    {
        long size;
        [size_is(size)] long * pData;
    } HDATA;

    typedef HDATA * WIRE_TYPE;
    typedef [wire_marshal(WIRE_TYPE)] void * HANDLE_DATA;
    ```

    Note that the wire type, **WIRE\_TYPE**, is a pointer type. Your HANDLE\_DATA\_UserMarshal function marshals the data related to the handle, using the HDATA layout, rather than the HDATA \* layout.

-   A wire-type must be either a flat data type or a pointer type. If your transmissible type must be something else (a structure with pointers, for example), use a pointer to your desired type as the wire-type.

The effect of these restrictions is that the types defined with the \[[**wire\_marshal**](/windows/desktop/Midl/wire-marshal)\] or \[[**user\_marshal**](/windows/desktop/Midl/user-marshal)\] attributes can be freely embedded in other types.

## Related topics

<dl> <dt>

[**wire\_marshal**](/windows/desktop/Midl/wire-marshal)
</dt> <dt>

[**user\_marshal**](/windows/desktop/Midl/user-marshal)
</dt> <dt>

[The type\_UserSize Function](the-type-usersize-function.md)
</dt> <dt>

[The type\_UserMarshal Function](the-type-usermarshal-function.md)
</dt> <dt>

[Thetype\_UserUnMarshalFunction](the-type-userunmarshal-function.md)
</dt> <dt>

[Thetype\_UserFreeFunction](the-type-userfree-function.md)
</dt> </dl>

 

 

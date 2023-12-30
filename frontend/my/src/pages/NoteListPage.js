import React, { useEffect, useState } from 'react';
import ListItem from '../components/ListItem';
const api=process.env.REACT_APP_API_URL;
const NoteListPage = () => {
    const [notes,setNotes] = useState([]);

    useEffect(()=>{
        getNotes();
    },[])

    let getNotes = async () => {
      let res = await fetch(`${api}/notes/`)
      let data = await res.json()
      setNotes(data)
    }

    return (
        <div>
            <h2>Notes List</h2>
            {notes.map((note,id)=>{
                return(
                   
                    <ListItem key={id} note={note}></ListItem>
                )
              
            })}
        </div>
    );
};

export default NoteListPage;
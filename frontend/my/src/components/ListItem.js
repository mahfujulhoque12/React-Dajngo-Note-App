import React from 'react';

const ListItem = ({note}) => {
    return (
        <div>
             <h4>{note.body}</h4>
        </div>
    );
};

export default ListItem;
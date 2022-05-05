import React from 'react';

export const Form = ({ onSubmit }) => {
  return (
    <form onSubmit={onSubmit}>
      <div className="form-group">
        <label htmlFor="name1">First Name</label>
        <input className="form-control" id="name1" />
      </div>
      <div className="form-group">
        <label htmlFor="name2">Last Name</label>
        <input className="form-control" id="name2" />
      </div>
      <div className="form-group">
        <button className="form-control btn btn-primary" type="submit">
          Submit
        </button>
      </div>
    </form>
  );
};
export default Form;

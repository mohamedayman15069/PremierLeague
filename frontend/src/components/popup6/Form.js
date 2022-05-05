import React from 'react';

export const Form = ({ onSubmit }) => {
  return (
    <form onSubmit={onSubmit}>
      <div className="form-group">
        <label htmlFor="name">Season</label>
        <input className="form-control" id="season" />
      </div>

      <div className="form-group">
        <label htmlFor="name">Home Team</label>
        <input className="form-control" id="hometeam" />
      </div>
      <div className="form-group">
        <label htmlFor="name">Away Team</label>
        <input className="form-control" id="awayteam" />
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

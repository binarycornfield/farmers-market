import { useState, useEffect } from "react";

const PWD_REGEX = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,24}$/;

const Register = () => {
  const [formData, setFormData] = useState({
    firstName: "",
    lastName: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Add your registration logic here, like sending the form data to a server
    console.log(formData);
    // Reset the form after submission
    setFormData({
      firstName: "",
      lastName: "",
      email: "",
      password: "",
      confirmPassword: "",
    });
  };

  return (
    <section>
      <div className="mb-4">
        <h1>Register</h1>
      </div>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label className="form-label" htmlFor="firstName">
            First Name
          </label>
          <input
            className="form-control"
            type="text"
            id="firstName"
            name="firstName"
            placeholder="First Name"
            onChange={handleChange}
            value={formData.firstName}
            required
          />
        </div>
        <div className="mb-3">
          <label className="form-label" htmlFor="lastName">
            Last Name
          </label>
          <input
            className="form-control"
            type="text"
            id="firstName"
            placeholder="Last Name"
            onChange={handleChange}
            value={formData.lastName}
          />
        </div>
        <div className="mb-3">
          <label className="form-label" htmlFor="email">
            Email
          </label>
          <input
            className="form-control"
            type="email"
            id="email"
            name="email"
            placeholder="Email"
            autoComplete="off"
            onChange={handleChange}
            value={formData.email}
            required
          />
        </div>
        <div className="mb-3">
          <label className="form-label" htmlFor="password">
            Password
          </label>
          <input
            className="form-control"
            type="password"
            name="password"
            id="password"
            placeholder="Password"
            onChange={handleChange}
            value={formData.password}
          />
        </div>
        <div className="mb-3">
          <label className="form-label" htmlFor="confirmPassword">
            Confirm Password
          </label>
          <input
            className="form-control"
            type="password"
            name="confirmPassword"
            id="confirmPassword"
            placeholder="Confirm password"
            onChange={handleChange}
            value={formData.confirmPassword}
          />
        </div>
        <button className="btn btn-primary" type="submit">
          Register
        </button>
      </form>
    </section>
  );
};

export default Register;

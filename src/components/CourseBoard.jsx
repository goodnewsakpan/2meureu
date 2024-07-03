import { NavLink } from "react-router-dom";

import Nav from "./Nav";
import styles from './CourseBoard.module.css'

export default function CourseBoard() {
  return (
    <div className={styles.courseBoard}>
        <Nav />

        <section className={styles.sectionCourseBoard}>
        <h2>Courses</h2>
        <ul>
            <li>
                <NavLink>All Courses</NavLink>
            </li>

            <li>
                <NavLink>In-Progress</NavLink>
            </li>

            <li>
                <NavLink>Outstanding</NavLink>
            </li>

            <li>
                <NavLink>Completed</NavLink>
            </li>
        </ul>

        <div className={styles.filter}>
            <input type="search" placeholder="search by course name or category" />
            <select>
                <option>Sort</option>
                <option>Title</option>
                <option>Course</option>
            </select>
        </div>
    </section>
    </div>
  )
}

import { NavLink } from 'react-router-dom'
import styles from './CourseSidebar.module.css'

export default function CourseSidebar() {
  return (
    <section className={styles.courseSidebar}>
        <div className={styles.logo}>
            <img src="" alt="lms-logo" />
        </div>
        <ul>
            <NavLink>
                <li>
                    {/* <img src="" alt="child img" /> */}
                    <span>My Child's <br /> information</span>
                </li>
            </NavLink>

            <NavLink>
                <li>
                    {/* <img src="" alt="child img" /> */}
                    <span>My Child's <br /> Results</span>
                </li>
            </NavLink>

            <NavLink>
                <li>
                    {/* <img src="" alt="child img" /> */}
                    <span>Payments and <br /> billings</span>
                </li>
            </NavLink>

            <NavLink>
                <li>
                    {/* <img src="" alt="child img" /> */}
                    <span>Account and <br /> Settings</span>
                </li>
            </NavLink>
        </ul>
    </section>
  )
}

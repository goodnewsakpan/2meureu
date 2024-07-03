import { NavLink } from 'react-router-dom'
import styles from './Nav.module.css'

export default function Nav() {
  return (
    <nav className={styles.navBar}>
        <ul>
            <li>
                <NavLink>About Us</NavLink>
            </li>

            <li>
                <NavLink>Contact Us</NavLink>
            </li>
        </ul>

        <div className={styles.notification}>
            <img src='' alt='notification-pics' />
        </div>

        <div className={styles.profilePics}>
            <img src='' alt='profile-pics' />
        </div>
    </nav>
  )
}
